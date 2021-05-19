from dotenv import load_dotenv
from pathlib import Path  # python3 only
import os

# set path to env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Config:
    """Set Flask configuration vars from .env file."""

    # Load in enviornemnt variables
    # TESTING = os.getenv('TESTING')
    # FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    # SERVER = os.getenv('SERVER')
    SECRET_KEY = os.getenv('SECRET_KEY')