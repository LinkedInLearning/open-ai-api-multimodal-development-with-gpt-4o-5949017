import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

def openai_init():
    """
    Initialize the OpenAI client object.

    Returns:
    obj: The OpenAI client object.
    """
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    return client