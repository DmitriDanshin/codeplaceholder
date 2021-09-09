from uvicorn import run
from fastapi import FastAPI
from src.codeplaceholder.tables import Base
from src.codeplaceholder.database import engine
from api import router

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    run("app:app", host="127.0.0.1", port=5000, log_level="info", reload=True)
