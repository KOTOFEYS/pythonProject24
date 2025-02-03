
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
import uvicorn

from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from routers import *
from routers import router as router_pages
from routers_users_backend import router as routers_page_users

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True, tags=["Backend"])
app.include_router(router_pages)
app.include_router(routers_page_users)
app.mount('/static', StaticFiles(directory='static'), 'static')
templates = Jinja2Templates(directory="templates")

@app.get('/all_base', tags=["Backend"])
async def all_base(db: Annotated[Session, Depends(get_db)]):
    query = text("SELECT * FROM users")
    result = db.execute(query).fetchall()
    return [Person(id=row.id, name=row.name, num_tel=row.num_tel) for row in result]
    db.commit()

@app.put('/apdate', tags=["Backend"])
async def update_person(user_id:int, db: Annotated[Session, Depends(get_db)], create_users:CreateUsers):
    select_query = text("SELECT * FROM users WHERE id = :id")
    result = db.execute(select_query, {"id": user_id}).fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="Person not found")
    update_query = text("UPDATE users SET name = :name, num_tel = :num_tel WHERE id = :id")
    db.execute(update_query,{"id": user_id, "name": create_users.name, "num_tel": create_users.num_tel})
    db.commit()
    updated_result = db.execute(select_query, {"id": user_id}).fetchone()
    return Person(id=updated_result.id, name=updated_result.name, num_tel=updated_result.num_tel)

@app.delete('/delete/{user_id}', tags=["Backend"])
async def delete_user(user_id:int, db: Annotated[Session, Depends(get_db)], create_users:CreateUsers):
    select_query = text("SELECT * FROM users WHERE id = :id")
    result = db.execute(select_query, {"id": user_id}).fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="Person not found")
    delete_query = text("DELETE FROM users WHERE id = :id")
    db.execute(delete_query, {"id": user_id})
    db.commit()
    return {"message": "Person deleted"}







if __name__ == '__main__':
    uvicorn.run("salon:app",host='127.0.0.1',port = 8000, reload = True)


