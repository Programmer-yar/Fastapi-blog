# Project Structure:
# app/
# ├── __init__.py
# ├── main.py
# ├── database.py
# ├── models/
# │   ├── __init__.py
# │   └── models.py
# ├── schemas/
# │   ├── __init__.py
# │   ├── user.py
# │   └── post.py
# ├── routers/
# │   ├── __init__.py
# │   ├── users.py
# │   └── posts.py
# └── dependencies.py

# ============= app/main.py =============
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.database import engine, Base
from routers import users, post

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CRUD API",
    version="1.0.0",
    description="A modular FastAPI CRUD application"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router)
app.include_router(post.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to the CRUD API",
        "docs": "/docs",
        "users_endpoint": "/users/",
        "posts_endpoint": "/posts/"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)