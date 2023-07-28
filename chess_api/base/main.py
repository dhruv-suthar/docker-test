from fastapi import FastAPI

app = FastAPI()

# Import the chess routes
from base.routes import chess

# Include the chess routes
app.include_router(chess.router)