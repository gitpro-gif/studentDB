from fastapi import FastAPI
from app.database.connection import Base, engine
from app.routes.student_routes import userrouter

app = FastAPI()

app.include_router(userrouter)

Base.metadata.create_all(bind=engine)

@app.get("/")
def healthcheck():
    return {"message": "Working"}