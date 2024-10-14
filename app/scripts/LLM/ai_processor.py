import google.generativeai as genai
import os
from scripts.logging_config import logger
from utils.utils import UserInput, FilterdOutputFromAI
from openai import OpenAI

class ai_processor():
    @staticmethod
    def ai_processor_func(user_input: UserInput):
        try:

            temperature = 0
            client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

            logger.info("=============AI process starting =============")
            # genai.configure(api_key=os.environ["GEMINI_API_KEY"])
            # model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            appended_data = dept_append(user_input.message)
            system_prompt = ger_system_prompt()
            # result = model.generate_content(
            #     appended_data,
            #     generation_config=genai.GenerationConfig(
            #     response_mime_type="application/json", 
            #     response_schema=FilterdOutputFromAI),)
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": appended_data}
            ]     

            try:
                response = client.beta.chat.completions.parse(
                    model="gpt-4o-mini-2024-07-18",
                    messages=messages,
                    response_format=FilterdOutputFromAI
                )
                logger.info(f"Response -> |{response}|")
                structured_output = response.choices[0].message
                logger.info(f"Structured Output -> |{structured_output}|{type(structured_output)}")
                logger.info(f"Structured refusal ->|{structured_output.refusal}|")
                logger.info(f"Structured parsed ->|{structured_output.parsed}")
                if structured_output.parsed:
                    return structured_output.parsed
                else:
                    return structured_output.refusal
            except Exception as e:
                logger.error(e)
        except Exception as e:
            logger.error(e, exc_info=True)
            raise


def ger_system_prompt():
    logger.info("text extracting from the text file starting")
    try:
        with open('LLM/prompts/system_prompt.txt', 'r') as file:
            file_content = file.read()
            logger.info("text extracting from the text file finished")
    except Exception as e:
        logger.error(e, exc_info=True)
        raise
    return file_content







def dept_append(user_message):
    logger.info("text extracting from the text file starting")
    try:
        with open('LLM/departments/dept.txt', 'r') as file:
            file_content = file.read()
            logger.info("text extracting from the text file finished")
    except Exception as e:
        logger.error(e, exc_info=True)
        raise
    return f"{user_message}\n" + file_content