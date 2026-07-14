from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.auth import LoginRequest
from app.security.jwt import create_access_token
from app.security.password import verify_password


class AuthService:

    @staticmethod
    def login(
        db: Session,
        credentials: LoginRequest,
    ):
        user = UserRepository.get_by_email(
            db,
            credentials.email,
        )

        if user is None:
            return None

        if not verify_password(
            credentials.password,
            user.password,
        ):
            return None

        token = create_access_token(
            {
                "sub": user.id,
                "email": user.email,
                "role": user.role,
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }
