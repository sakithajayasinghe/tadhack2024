from pydantic import BaseModel
from dataclasses import dataclass


class UserInput(BaseModel):
    requestId: str
    message: str

@dataclass
class FilterdOutputFromAI():
    rephrasedQuestion: str
    briefExplaination: str
    answerForCustomer: str
