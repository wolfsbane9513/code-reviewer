# config/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GITHUB_KEY = os.getenv("GITHUB_KEY")
    NOTION_KEY = os.getenv("NOTION_KEY")
    NOTION_PAGE_ID = '14b322bb-b8bc-80a4-98ca-c7f7c0090baa'
    IGNORE_DIRS = {'public', 'images', 'media', 'assets'}
    MAX_FILE_SIZE = 1000000  # 1MB
    MAX_LINES = 500