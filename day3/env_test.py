
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

app_name = os.getenv("APP_NAME")
app_env = os.getenv("APP_ENV")
api_timeout = os.getenv("API_TIMEOUT")
api_key = os.getenv("API_KEY")

print("App Name:", app_name)
print("Environment:", app_env)
print("API Timeout:", api_timeout)
print("API Key loaded:", bool(api_key))


