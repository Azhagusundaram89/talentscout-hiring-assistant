import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="talentscout"
    )

def save_candidate(data):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO candidates 
    (name, email, phone, experience, role, location, tech_stack)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        data["name"],
        data["email"],
        data["phone"],
        data["experience"],
        data["role"],
        data["location"],
        data["tech_stack"]
    )

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()