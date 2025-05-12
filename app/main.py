from fastapi import FastAPI
from app.api import cart, order, user, offers, chat

app = FastAPI(title="Shop Assistant API")

# Include routers for each feature
app.include_router(cart.router, prefix="/cart", tags=["Cart"])
app.include_router(order.router, prefix="/order", tags=["Order"])
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(offers.router, prefix="/offers", tags=["Offers"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

# Health check endpoint
define_health = lambda: {"status": "ok"}
app.get("/health")(define_health)
