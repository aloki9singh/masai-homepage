from flask import request, jsonify
from app import app
from app.services.user_service import find_user
from app.exceptions.custom_exceptions import CustomException


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
