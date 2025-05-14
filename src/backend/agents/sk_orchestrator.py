# Semantic Kernel Orchestrator stub
# This class is the entry point for all user messages from FastAPI.
# It classifies intent and routes to the appropriate agent/skill.

from .cart_agent import ShoppingCartManagementAgent
from .order_agent import OrderManagementAgent
from .personalization_agent import PersonalizationAgent

class SemanticKernelOrchestrator:
    def __init__(self):
        # Initialize SK, load skills/agents, etc.
        self.cart_agent = ShoppingCartManagementAgent()
        self.order_agent = OrderManagementAgent()
        self.personalization_agent = PersonalizationAgent()

    def classify_intent(self, message: str) -> str:
        # Simple mock intent classifier (replace with SK/LLM in production)
        msg = message.lower()
        if "cart" in msg or "add" in msg or "remove" in msg:
            return "cart"
        elif "order" in msg or "buy" in msg or "checkout" in msg:
            return "order"
        elif "recommend" in msg or "suggest" in msg or "offer" in msg:
            return "personalization"
        else:
            return "unknown"

    def handle_message(self, user_id: int, message: str, context: dict = None) -> dict:
        intent = self.classify_intent(message)
        if intent == "cart":
            # Call cart agent (mock)
            response = self.cart_agent.get_cart(user_id)
            return {
                "response": f"Cart agent called. Cart: {response}",
                "actions": ["cart"],
                "context": context or {}
            }
        elif intent == "order":
            # Call order agent (mock)
            response = self.order_agent.place_order(user_id, cart=None)
            return {
                "response": f"Order agent called. Order: {response}",
                "actions": ["order"],
                "context": context or {}
            }
        elif intent == "personalization":
            # Call personalization agent (mock)
            response = self.personalization_agent.recommend_products(user_id)
            return {
                "response": f"Personalization agent called. Recommendations: {response}",
                "actions": ["personalization"],
                "context": context or {}
            }
        else:
            return {
                "response": f"Sorry, I didn't understand: {message}",
                "actions": ["unknown"],
                "context": context or {}
            }
