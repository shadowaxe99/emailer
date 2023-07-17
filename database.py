import sqlite3
from sqlite3 import Error

# Define the schemas for the tables
UserSchema = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    preferences TEXT NOT NULL,
    schedule TEXT NOT NULL
);
"""

AppointmentSchema = """
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    appointment TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

ScheduleSchema = """
CREATE TABLE IF NOT EXISTS schedules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    schedule TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""


def create_connection():
    conn = None
    try:
        # creates a memory-based SQLite database
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
    except Error as e:
        print(e)

    if conn:
        return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def store_data(user_preferences, user_schedule, user_appointments):
    conn = create_connection()

    if conn is not None:
        # create tables
        create_table(conn, UserSchema)
        create_table(conn, AppointmentSchema)
        create_table(conn, ScheduleSchema)

        # store user data
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users(preferences, schedule) VALUES(?,?)",
            (user_preferences,
             user_schedule))
        user_id = cur.lastrowid

        # store appointments
        for appointment in user_appointments:
            cur.execute(
                "INSERT INTO appointments(user_id, appointment) VALUES(?,?)",
                (user_id,
                 appointment))

        # commit the transactions
        conn.commit()

        # close the connection
        conn.close()
    else:
        print("Error! cannot create the database connection.")