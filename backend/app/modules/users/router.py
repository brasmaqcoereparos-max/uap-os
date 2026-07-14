from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.user import UserCreate
from app.modules.users.service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/")
def list_users(db: Session = Depends(get_db)):
    return UserService.list(db)


@router.get("/{user_id}")
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = UserService.get(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.post("/")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return UserService.create(
        db=db,
        name=user.name,
        email=user.email,
        password=user.password,
    )


@router.delete("/{user_id}")
def delete_user(
    user_id: str,
    db: Session = Depends(get_db),
):
    deleted = UserService.delete(db, user_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted successfully"}
