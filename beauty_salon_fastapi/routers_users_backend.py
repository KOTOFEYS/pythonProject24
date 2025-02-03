from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import Annotated
from backend.db_depends import get_db
from models import Person
from schemas import CreateUsers

router = APIRouter(prefix="",tags=["Backend"],)
DbSession = Annotated[Session, Depends(get_db)]

# @router.get("/get", response_model=list[CreateUsers])
# def get_all_users(db: DbSession):
#     query = text("SELECT * FROM users")
#     result = db.execute(query).fetchall()
#     return [Person(id=row.id, username=row.name, num_tel=row.num_tel) for row in result]
#
# @router.post("/create", response_model=CreateUsers)
# def create_users(create_users: CreateUsers, db: DbSession):
#
#     query = text("INSERT INTO users (username, num_tel) VALUES (:name, :num_tel)")
#     db.execute(query, {"username": create_users.username, "num_tel": create_users.num_tel})
#     db.commit()
# Возвращаем созданную категорию
#     select_query = text("SELECT * FROM create_users WHERE name = :name")
#     result = db.execute(select_query, {"name": create_users.name}).fetchone()
#     return Person(id=result.id, name=result.name, num_tel=result.num_tel)