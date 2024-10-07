from fastapi import FastAPI
from utils.utils import UserInput
from scripts.logging_config import logger
from scripts.LLM.ai_processor import ai_processor
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()


# def open_ai_process():


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/filter")
async def filter(user_input: UserInput):
    logger.info("Request Received.")
    ai_process = ai_processor()
    response = ai_process.ai_processor_func(user_input) 
    return {"message": response}