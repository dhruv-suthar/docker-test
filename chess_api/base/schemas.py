from pydantic import BaseModel
from typing import Dict

class ChessPositionsSchema(BaseModel):
    positions: Dict[str, str]   