from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserService:

    @staticmethod
    def list(db: Session):
        return UserRepository.list(db)

    @staticmethod
    def get(db: Session, user_id: str):
        return UserRepository.get(db, user_id)

    @staticmethod
    def create(
        db: Session,
        name: str,
        email: str,
        password: str,
    ):
        user = User(
            name=name,
            email=email,
            password=password,
        )

        return UserRepository.create(db, user)

    @staticmethod
    def delete(
        db: Session,
        user_id: str,
    ):
        user = UserRepository.get(db, user_id)

        if not user:
            return False

        UserRepository.delete(db, user)

        return True
