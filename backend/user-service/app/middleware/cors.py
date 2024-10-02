from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
origins = ["*"]

def configure_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=True,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

