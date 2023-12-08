from datetime import datetime
from pydantic import BaseModel


class GameBase(BaseModel):
    name: str
    difficulty: str
    start_time: datetime
    end_time: datetime
    stadium_id: int
    count_participant: int


class GameCreate(BaseModel):
    name: str
    difficulty: str
    start_time: datetime
    end_time: datetime
    stadium_id: int


class Game(GameBase):
    id: int

    class Config:
        orm_mode = True
