import sqlite3

from fastmcp import FastMCP

mcp = FastMCP("Patient")

DB_PATH = "mcp_servers/patients.db"


@mcp.tool()
def get_patient_by_id(patient_id: int) -> str:
    """Get a patient's details by their patient ID."""
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, age, gender, blood_group, condition FROM patients WHERE id = ?", (patient_id,))
    row = cursor.fetchone()
    connection.close()

    if row is None:
        return f"No patient found with ID {patient_id}."
    return f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}, Blood Group: {row[4]}, Condition: {row[5]}"


@mcp.tool()
def search_by_blood_group(blood_group: str) -> str:
    """Search for patients by blood group, e.g. A+, O-, AB+."""
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, age FROM patients WHERE blood_group = ?", (blood_group,))
    rows = cursor.fetchall()
    connection.close()

    if not rows:
        return f"No patients found with blood group {blood_group}."
    lines = [f"ID: {r[0]}, Name: {r[1]}, Age: {r[2]}" for r in rows]
    return "\n".join(lines)


@mcp.tool()
def list_all_patients() -> str:
    """List all patients with their name, age, and blood group."""
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, age, blood_group FROM patients")
    rows = cursor.fetchall()
    connection.close()

    lines = [f"ID: {r[0]}, Name: {r[1]}, Age: {r[2]}, Blood Group: {r[3]}" for r in rows]
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8003)
