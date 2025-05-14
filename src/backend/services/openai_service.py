# Azure OpenAI integration

# Azure OpenAI integration service
class OpenAIService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        # TODO: Initialize Azure OpenAI client

    def generate_response(self, prompt: str) -> str:
        # TODO: Call Azure OpenAI API and return response
        return "This is a mock OpenAI response."
