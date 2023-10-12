from app import mysql


def insert_user(user):
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO users (full_name, email, phone) VALUES (%s, %s, %s)",
        (user.full_name, user.email, user.phone),
    )
    mysql.connection.commit()
    cur.close()






