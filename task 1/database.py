import sqlite3
from faker import Faker
from datetime import datetime, timedelta
import random

# Initialize Faker for generating random data
fake = Faker()

# Function to create a SQLite database and populate it with random data
def create_and_populate_database(database_name='test.db', num_users=10, num_orders=20):
    # Connect to SQLite database
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Create 'users' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    ''')

    # Create 'orders' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            order_date DATE,
            total_amount REAL,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    ''')

    # Generate random user data and insert into 'users' table
    for _ in range(num_users):
        user_data = (fake.name(), fake.email())
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', user_data)

    # Generate random order data and insert into 'orders' table
    for _ in range(num_orders):
        order_data = (
            random.randint(1, num_users),  # Random user_id
            fake.date_time_between(start_date='-30d', end_date='now'),  # Random order_date in the last 30 days
            random.uniform(10, 1000)  # Random total_amount
        )
        cursor.execute('INSERT INTO orders (user_id, order_date, total_amount) VALUES (?, ?, ?)', order_data)

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Run the function to create and populate the database
create_and_populate_database()

print("Database created and populated with random data.")
