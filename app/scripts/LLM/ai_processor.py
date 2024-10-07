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

            result = model.generate_content(
                user_input.message,
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