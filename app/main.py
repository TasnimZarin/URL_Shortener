from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.database import engine, Base
from app.models import url
from app.routes import url as url_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(url_routes.router)

@app.get("/")
def root():
    return FileResponse("app/static/index.html")