import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Suroj@725",
    database="admin_login_system"
)

cursor = conn.cursor(dictionary=True)