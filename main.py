from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router


# uvicorn main:app --reload  ------ for start app

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова")
    yield
    print("Выключение")
    # Clean up the ML models and release the resources


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)  # добавление нового роутера

