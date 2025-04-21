import psycopg2
import pandas as pd

# Database connection parameters
db_params = {
    'database': 'your_database',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'port': '5432'
}

# Connect to PostgreSQL
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Read CSV files
employees_df = pd.read_csv('employees.csv')
managers_df = pd.read_csv('managers.csv')

# Create tables
create_employees_table = """
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100),
    role VARCHAR(50)
);"""

create_managers_table = """
CREATE TABLE IF NOT EXISTS managers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100),
    role VARCHAR(50)
);"""

cursor.execute(create_employees_table)
cursor.execute(create_managers_table)

# Insert data
for _, row in employees_df.iterrows():
    cursor.execute(
        "INSERT INTO employees (id, name, email, password, role) VALUES (%s, %s, %s, %s, %s)",
        (row['ID'], row['Name'], row['Email'], row['Password'], row['Role'])
    )

for _, row in managers_df.iterrows():
    cursor.execute(
        "INSERT INTO managers (id, name, email, password, role) VALUES (%s, %s, %s, %s, %s)",
        (row['ID'], row['Name'], row['Email'], row['Password'], row['Role'])
    )

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()