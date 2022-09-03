from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . routers import note

app = FastAPI()

origins = ["*"]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

app.include_router(note.router)

@app.get("/")
def root():
    return {"message": "Welcome, Hello World!!!"}
