from pydantic import BaseModel
from dataclasses import dataclass
from enum import Enum, IntEnum

class UserInput(BaseModel):
    requestId: str
    message: str

class PriorityLevel(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class FilterdOutputFromAI(BaseModel):
    rephrasedQuestion: str
    relventDepartment: str
    replyMessage: str
    priorityLevel: PriorityLevel

    

