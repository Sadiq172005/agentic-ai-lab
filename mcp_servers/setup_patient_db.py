import sqlite3

connection = sqlite3.connect("mcp_servers/patients.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS patients")
cursor.execute("""
    CREATE TABLE patients (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gender TEXT,
        blood_group TEXT,
        condition TEXT
    )
""")

patients = [
    (1, "Amit Sharma", 34, "Male", "B+", "Diabetes"),
    (2, "Priya Verma", 28, "Female", "O+", "Asthma"),
    (3, "Rahul Singh", 45, "Male", "A+", "Hypertension"),
    (4, "Sneha Patel", 22, "Female", "AB+", "Healthy"),
    (5, "Vikram Rao", 60, "Male", "O-", "Heart Disease"),
    (6, "Anjali Gupta", 31, "Female", "B-", "Migraine"),
    (7, "Karan Mehta", 50, "Male", "A-", "Diabetes"),
    (8, "Neha Joshi", 26, "Female", "AB-", "Healthy"),
    (9, "Suresh Kumar", 55, "Male", "O+", "Arthritis"),
    (10, "Divya Nair", 19, "Female", "B+", "Healthy"),
    (11, "Rajesh Iyer", 40, "Male", "A+", "Hypertension"),
    (12, "Pooja Reddy", 33, "Female", "O+", "Thyroid"),
    (13, "Manoj Tiwari", 47, "Male", "B+", "Diabetes"),
    (14, "Kavita Desai", 29, "Female", "A-", "Asthma"),
    (15, "Arjun Malhotra", 38, "Male", "AB+", "Healthy"),
    (16, "Ritu Chawla", 24, "Female", "O-", "Migraine"),
    (17, "Deepak Yadav", 52, "Male", "B-", "Heart Disease"),
    (18, "Swati Kulkarni", 36, "Female", "A+", "Thyroid"),
    (19, "Nikhil Bansal", 42, "Male", "O+", "Hypertension"),
    (20, "Meera Pillai", 27, "Female", "AB-", "Healthy"),
]

cursor.executemany("INSERT INTO patients VALUES (?, ?, ?, ?, ?, ?)", patients)

connection.commit()
connection.close()

print("patients.db created with 20 patient records.")
