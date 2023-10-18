import unittest
import json
from app import app
import requests
from unittest.mock import patch


class TestSignupAPI(unittest.TestCase):
    base_url = "https://kapil7982.pythonanywhere.com"

    def test_successful_signup(self):
        url = f"{self.base_url}/signup"
        payload = {
            "full_name": "Pablo Kumar",
            "email": "pablo@gmail.com",
            "phone": "7531596488",
        }

        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn("User registered successfully.", response.json()["message"])

    def test_failed_signup_existing_email(self):
        url = "https://kapil7982.pythonanywhere.com/signup"
        existing_user_data = {
            "full_name": "Rohit Kumar",
            "email": "ravi@gmail.com",
            "phone": None,
        }

        response = requests.post(url, json=existing_user_data)

        self.assertEqual(response.status_code, 400)
        expected_message = {
            "error": "('User already registered with this email or phone.', 400)"
        }
        self.assertEqual(response.json(), expected_message)

    def test_failed_signup_empty_full_name(self):
        url = f"{self.base_url}/signup"
        payload = {"full_name": "", "email": "johndoe@example.com", "phone": None}

        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "Invalid request. Provide full name and either email or phone.",
            response.json()["error"],
        )

    def test_failed_signup_missing_email_and_phone(self):
        url = f"{self.base_url}/signup"
        payload = {"full_name": "John Doe", "email": None, "phone": None}

        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "Invalid request. Provide full name and either email or phone.",
            response.json()["error"],
        )

    def test_failed_signup_invalid_email_format(self):
        url = f"{self.base_url}/signup"
        payload = {
            "full_name": "John Doe",
            "email": "invalidemail",
            "phone": None,
        }

        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid email format.", response.json()["error"])

    def test_failed_signup_invalid_request(self):
        url = f"{self.base_url}/signup"
        payload = {}

        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "Invalid request. Provide full name and either email or phone.",
            response.json()["error"],
        )

    def test_successful_otp_generation_with_email(self):
        url = f"{self.base_url}/login"
        payload = {
            "email": "pablo@gmail.com",
            "phone": None,
        }

        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("OTP sent successfully.", response.json()["message"])
        self.assertIn("otp", response.json())

    def test_failed_login_invalid_request(self):
        url = f"{self.base_url}/login"
        payload = {}

        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "Invalid request. Provide either email or phone.", response.json()["error"]
        )

    def test_failed_login_both_email_and_phone(self):
        url = f"{self.base_url}/login"
        payload = {
            "email": "",
            "phone": "",
        }

        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "Invalid request. Provide either email or phone.", response.json()["error"]
        )

    def test_failed_login_user_not_found_with_email(self):
        url = f"{self.base_url}/login"
        payload = {
            "email": "nonexistent@example.com",  # Provide the non-existing email
            "phone": None,
        }

        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 404)
        self.assertIn("User not found.", response.json()["error"])

    def test_failed_login_user_not_found_with_phone(self):
        url = f"{self.base_url}/login"
        payload = {
            "email": None,
            "phone": "9999999999",  # Provide a non-existing phone number in your database
        }

        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 404)
        self.assertIn("User not found.", response.json()["error"])

    def test_successful_verification(self):
        url = f"{self.base_url}/verify_otp"
        payload = {
            "otp_code": "501112"
        }  # Assuming "valid_otp_code" is a valid OTP code in your database

        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("email", response.json())

    def test_failed_verification_invalid_request(self):
        url = f"{self.base_url}/verify_otp"
        payload = {}

        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "Invalid request. Provide the OTP code.", response.json()["error"]
        )

    def test_failed_verification_invalid_otp(self):
        url = f"{self.base_url}/verify_otp"
        payload = {
            "otp_code": "456789"
        }  # Assuming "invalid_otp_code" is not a valid OTP code in your database

        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid OTP or OTP has expired.", response.json()["error"])

    def test_failed_verification_expired_otp(self):
        url = f"{self.base_url}/verify_otp"
        payload = {
            "otp_code": "689410"
        }  # Assuming "expired_otp_code" is an expired OTP code in your database

        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid OTP or OTP has expired.", response.json()["error"])
