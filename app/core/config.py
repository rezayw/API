from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "FastAPI App")
API_PREFIX = os.getenv("API_PREFIX", "/api")
