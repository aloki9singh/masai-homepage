from flask import request, jsonify, abort
from app import app
import re
from app.services.user_service import create_user, find_user
from app.exceptions.custom_exceptions import CustomException
from flask_cors import CORS
from MySQLdb import IntegrityError

CORS(app)


@app.route("/")
def home():
    return "Hello!"


@app.route("/signup", methods=["POST"])
def signup():
    try:
        data = request.get_json()
        full_name = data.get("full_name")
        email = data.get("email")
        phone = data.get("phone")

        if not (full_name and email and phone):
            raise CustomException(
                "Invalid request. Provide full name and either email and phone number.",
                400,
            )

        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise CustomException("Invalid email format.", 400)

        if phone and not re.match(r"^\d{10}$", phone):
            raise CustomException(
                "Invalid phone format. Please provide a 10-digit phone number.", 400
            )

        existing_user = find_user(email, phone)
        if existing_user:
            raise CustomException(
                "User already registered with this email or phone.", 400
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

        return (
            jsonify(
                {
                    "message": "Login successful.",
                    "user": {"email": user[2], "phone": user[3]},
                }
            ),
            200,
        )

    except CustomException as e:
        return jsonify({"error": str(e)}), e.status_code
