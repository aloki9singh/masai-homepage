from app.models.user import User
from app.repositories.user_repository import (
    insert_user,
    find_user_by_email,
    find_user_by_phone,
)


def find_user(email=None, phone=None):
    if email:
        return find_user_by_email(email)
    elif phone:
        return find_user_by_phone(phone)