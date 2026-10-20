from fastapi import FastAPI

app = FastAPI()






@app.get("/users")
def get_users():
    return {"users": ["Bipin", "Rahul"]}


#uv run uvicorn main:app --reload --port 8001