from fastapi import FastAPI
from app import auth, routes
from app.database import Base, engine
from app import models

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure Job Tracker API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(routes.router, prefix="/jobs", tags=["Jobs"])