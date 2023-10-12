from app import mysql


def insert_user(user):
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO users (full_name, email, phone) VALUES (%s, %s, %s)",
        (user.full_name, user.email, user.phone),
    )
    mysql.connection.commit()
    cur.close()


def find_user_by_email(email):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    cur.close()
    return user


def find_user_by_phone(phone):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE phone = %s", (phone,))
    user = cur.fetchone()
    cur.close()
    return user
