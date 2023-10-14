from app import mysql
from MySQLdb import IntegrityError
from app.exceptions.custom_exceptions import CustomException


def insert_user(user):
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO users (full_name, email, phone) VALUES (%s, %s, %s)",
            (user.full_name, user.email, user.phone),
        )
        mysql.connection.commit()
        cur.close()

    except IntegrityError as e:
        raise CustomException("User already exists.", 400)
    except Exception as e:
        raise CustomException("An unexpected error occurred.", 500)


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
