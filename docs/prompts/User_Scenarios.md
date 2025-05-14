# User Scenarios for Shopping Assistant

**Prompt**: Create user scenarios 

Agent created initial version. 

**Prompt**: I'd like to request you to update this User_Scenarios.md. We need to design sign in page that also allows a new user to perform registration process, so that we can create a new user in the user database. At this time, a new customer entry is also added to the customer database. If not a new user, the user can do sign in. I'd like the backend app generate token that contains user credentials and a token that is associated with this user, so that additional operations can be performed at subsequent steps such as placing a new order or making inquires about orders and products. See more details in [Security Tokens](Security_Tokens.md). 

This document outlines key user scenarios to illustrate how real users will interact with the Shopping Assistant. These scenarios help guide architecture, feature design, and development priorities.

---

## Scenario 0: User Registration, Sign-In, and Logout
**Persona:** Any new or returning user
- The user visits the Shopping Assistant web app and is presented with a sign-in/registration page.
- If the user is new, they can register by providing required information (e.g., username, email, password, and profile details).
- Upon successful registration:
    - A new user entry is created in the user database.
    - A corresponding customer entry is created in the customer database.
    - The user is automatically signed in.
- If the user is returning, they can sign in with their credentials.
- Upon successful sign-in (for both new and returning users):
    - The backend returns a secure authentication token (e.g., JWT) containing user credentials and identity.
    - This token is used for all subsequent operations (placing orders, making inquiries, etc.), ensuring secure and personalized access.
- **Logout:**
    - The user can log out at any time via a logout button or menu option.
    - Upon logout, the authentication token is invalidated or removed from the client, ending the session and requiring re-authentication for further actions.

## Scenario 1: New User Browses and Searches for Products
**Persona:** Alex, a first-time visitor
- Alex visits the Shopping Assistant web app.
- Alex uses the search bar to look for “wireless headphones.”
- The assistant displays a list of matching products with details and prices.
- Alex adds a pair of headphones to the shopping cart.

## Scenario 2: Personalized Product Recommendations
**Persona:** Jamie, a returning user
- Jamie logs in to their account.
- The assistant greets Jamie and suggests products based on previous purchases and preferences.
- Jamie explores recommended items and adds one to the cart.

## Scenario 3: Conversational Order Placement
**Persona:** Taylor, a busy shopper
- Taylor interacts with the chatbot UI, typing: “Order two bags of organic coffee.”
- The assistant confirms the product, quantity, and price, then asks for confirmation.
- Upon Taylor’s confirmation, the order is placed and a summary is shown.

## Scenario 4: Wishlist and Favorites
**Persona:** Morgan, a deal hunter
- Morgan browses products and adds several to their wishlist for future consideration.
- Morgan later moves a wishlist item to the shopping cart and proceeds to checkout.

## Scenario 5: Order Tracking and History
**Persona:** Riley, a frequent buyer
- Riley logs in and asks, “Where’s my last order?” via the chatbot.
- The assistant retrieves and displays the latest order status and tracking info.

## Scenario 6: Mock Payment and Checkout
**Persona:** Sam, a cautious buyer
- Sam reviews the cart and proceeds to checkout.
- The assistant uses a mock payment API to simulate payment processing.
- Sam receives a confirmation message and order summary.

## Scenario 7: Personalized Offers
**Persona:** Jordan, a loyal customer
- Jordan receives a personalized offer for a product frequently browsed.
- The assistant applies the offer at checkout, and Jordan completes the purchase.

---

These scenarios are designed to cover the core prioritized capabilities and provide a foundation for user-centric design and testing. Additional scenarios can be added as the project evolves.
