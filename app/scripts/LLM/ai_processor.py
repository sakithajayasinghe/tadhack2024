import google.generativeai as genai
import os
from scripts.logging_config import logger
from utils.utils import UserInput, FilterdOutputFromAI

class ai_processor():
    @staticmethod
    def ai_processor_func(user_input: UserInput):
        try:
            logger.info("=============AI process starting =============")
            genai.configure(api_key=os.environ["GEMINI_API_KEY"])
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            appended_data = dept_append(user_input.message)
            result = model.generate_content(
                appended_data,
                generation_config=genai.GenerationConfig(
                response_mime_type="application/json", 
                response_schema=FilterdOutputFromAI),)
            
            logger.info(result)
            logger.info("Response created and returned.")
            logger.info("=============AI process finished =============")
            return(result.text)
        except Exception as e:
            logger.error(e, exc_info=True)
            raise

def dept_append(user_message):
    logger.info("text extracting from the text file starting")
    try:
        with open('LLM/bank_departments/dept.txt', 'r') as file:
            file_content = file.read()
            logger.info("text extracting from the text file finished")
    except Exception as e:
        logger.error(e, exc_info=True)
        raise
    return f"{user_message}\n" + file_content