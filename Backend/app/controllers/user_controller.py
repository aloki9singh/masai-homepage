from flask import request, jsonify
from app import app
from app.services.user_service import create_user, find_user
from app.exceptions.custom_exceptions import CustomException


@app.route("/")
def home():
    return "hellow"

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

        create_user(full_name, email, phone)

        return jsonify({"message": "User registered successfully."}), 201

    except CustomException as e:
        return jsonify({"error": str(e)}), e.status_code


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

     

   