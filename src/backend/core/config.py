# App configuration utilities
import os

class Settings:
    def __init__(self):
        self.db_url = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/shopdb")
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "")
        self.search_endpoint = os.getenv("SEARCH_ENDPOINT", "")
        self.search_api_key = os.getenv("SEARCH_API_KEY", "")
        self.keyvault_url = os.getenv("KEYVAULT_URL", "")

settings = Settings()
