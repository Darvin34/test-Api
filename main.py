import uvicorn  # для запуска API
from fastapi import FastAPI
from database import engine, base
import router as UserRouter

base.metadata.create_all(bind=engine)   # подключение к бд
app = FastAPI()
app.include_router(UserRouter.router, prefix='/user')

if __name__ == '__main__':
    uvicorn.run("main:app",  reload=True)