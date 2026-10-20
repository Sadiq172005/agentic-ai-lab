from fastapi import FastAPI

app = FastAPI()

users = {
    1: {"name": "Bipin", "age": 30},
    2: {"name": "Rahul", "age": 25},
}


# GET
@app.get("/users")
def get_users():
    return users


# GET one user
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return users[user_id]


# POST
@app.post("/users")
def create_user(user: dict):
    user_id = max(users.keys()) + 1

    users[user_id] = user

    return {
        "id": user_id,
        "user": user
    }


# PUT
@app.put("/users/{user_id}")
def update_user(user_id: int, user: dict):
    users[user_id] = user

    return {
        "id": user_id,
        "user": user
    }


# DELETE
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    deleted_user = users.pop(user_id)

    return {
        "message": "User deleted",
        "user": deleted_user
    }