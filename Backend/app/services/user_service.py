from app.models.user import User
from app.repositories.user_repository import (
    insert_user,
  
)


def create_user(full_name, email, phone):
    user = User(full_name, email, phone)
    insert_user(user)

