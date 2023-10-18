from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from MySQLdb import IntegrityError
import re
from twilio.rest import Client
from datetime import datetime, timedelta

account_sid = "ACad34c751981b1389c2d38525ed2dc637"
auth_token = "cac2c0a82bcb02d0e9762ca5bbd7d8cf"
twilio_phone_number = "+1234567890"
client = Client(account_sid, auth_token)

otp_storage = {}


app = Flask(__name__)
CORS(app)

# MySQL Configuration
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "port"
app.config["MYSQL_DB"] = "flask_app"
mysql = MySQL(app)


def generate_otp():
    import random

    return str(random.randint(100000, 999999))


class User:
    def __init__(self, full_name, email, phone):
        self.full_name = full_name
        self.email = email
        self.phone = phone


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
        raise CustomException("User already registered with this email or phone.", 400)
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


def create_user(full_name, email, phone):
    user = User(full_name, email, phone)
    insert_user(user)


def find_user(email=None, phone=None):
    if email:
        return find_user_by_email(email)
    elif phone:
        return find_user_by_phone(phone)


class CustomException(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code


@app.route("/")
def home():
    return "hello"


@app.route("/signup", methods=["POST"])
def signup():
    try:
        data = request.get_json()
        full_name = data.get("full_name")
        email = data.get("email")
        phone = data.get("phone")

        if not (full_name and (email or phone)):
            raise CustomException(
                "Invalid request. Provide full name and either email or phone.", 400
            )

        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise CustomException("Invalid email format.", 400)

        if not email.endswith("@gmail.com"):
            raise CustomException("Only @gmail.com addresses are allowed.", 400)

        if phone and not re.match(r"^\d{10}$", phone):
            raise CustomException(
                "Invalid phone format. Please provide a 10-digit phone number.", 400
            )

        create_user(full_name, email, phone)

        return jsonify({"message": "User registered successfully."}), 201

    except CustomException as e:
        return jsonify({"error": str(e)}), e.status_code

    except IntegrityError as e:
        return jsonify({"error": "Email is already registered."}), 400

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500


@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        email = data.get("email")
        phone = data.get("phone")

        if not (email or phone):
            raise CustomException(
                "Invalid request. Provide either email or phone.", 400
            )

        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise CustomException("Invalid email format.", 400)

        if phone and not re.match(r"^\d{10}$", phone):
            raise CustomException(
                "Invalid phone format. Please provide a 10-digit phone number.", 400
            )

        user = find_user(email, phone)

        if not user:
            raise CustomException("User not found.", 404)

        # Generate OTP
        otp = generate_otp()

        # Store OTP in the database
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO otps (user_id, otp_code, expiration_time) VALUES (%s, %s, %s)",
            (
                user[0],
                otp,
                datetime.now() + timedelta(minutes=5),
            ),  # Expires in 5 minutes
        )
        mysql.connection.commit()
        cur.close()

        # Send OTP via SMS using Twilio
        if phone:
            message = client.messages.create(
                body=f"Your OTP is: {otp}", from_=twilio_phone_number, to=phone
            )
        else:
            # Send OTP via email (you'll need to implement this part)
            pass

        expiration_time = (datetime.now() + timedelta(minutes=5)).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        return (
            jsonify(
                {
                    "message": "OTP sent successfully.",
                    "otp_expiration": expiration_time,
                    "otp": otp,
                }
            ),
            200,
        )

    except CustomException as e:
        return jsonify({"error": str(e)}), e.status_code

    # except Exception as e:
    #     return jsonify({"error": "An unexpected error occurred."}), 500


@app.route("/verify_otp", methods=["POST"])
def verify_otp():
    try:
        data = request.get_json()
        otp_code = data.get("otp_code")

        if not otp_code:
            raise CustomException("Invalid request. Provide the OTP code.", 400)

        # Check if OTP is valid
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT users.email FROM otps JOIN users ON otps.user_id = users.id WHERE otps.otp_code = %s AND otps.expiration_time > NOW()",
            (otp_code,),
        )
        email = cur.fetchone()

        if not email:
            raise CustomException("Invalid OTP or OTP has expired.", 400)

        cur.close()

        return jsonify({"email": email[0]}), 200

    except CustomException as e:
        return jsonify({"error": str(e)}), e.status_code

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500


if __name__ == "__main__":
    app.run(debug=True)
