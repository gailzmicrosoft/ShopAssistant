# GitHub Copilot Agent Mode - Prompt 1:   Capabilities 

**Prompt**: I am starting a new project to create an online shopping assistant. Can you provide all the capabilities to be created?

**Agent**: Here are some essential capabilities and features you should consider for an online shopping assistant project:

1. Product Search: Allow users to search for products by name, category, or attributes.
2. Product Recommendations: Suggest products based on user preferences, browsing history, or trending items.
3. Shopping Cart Management: Add, remove, and update items in a virtual shopping cart.
4. Price Comparison: Compare prices across different vendors or platforms.
5. User Authentication: Register, log in, and manage user profiles securely.
6. Order Placement: Enable users to place orders and select payment/shipping options.
7. Order Tracking: Allow users to track the status of their orders.
8. Wishlist/Favorites: Let users save products for future reference.
9. Chatbot/Conversational UI: Provide a chat interface for users to interact with the assistant.
10. Notifications: Send alerts for deals, order updates, or restocks.
11. Reviews & Ratings: Display and collect product reviews and ratings.
12. Integration with Payment Gateways: Support secure online payments.
13. Customer Support: Offer help via chat, email, or FAQ.
14. Personalized Offers: Provide discounts or promotions tailored to the user.
15. Inventory Management (for sellers): Track stock levels and update product listings.

Would you like a breakdown of how to implement these features, or do you want to prioritize certain capabilities first?

**Prompt**: This is a great list. Also to let you know this is a quick experiment project.  The code will not have every function at this time. With that in mind, I would like to prioritize them as below: 

1. Product Search: Yes
2. Product Recommendations: Yes
3. Shopping Cart Management: Yes
4. Price Comparison: No at this time. Maybe in next version
5. User Authentication: Yes, would like to use the same database used in the application, Azure PostgreSQL Server to manage the backend authentication. Use a separate authentication DB. In addition, I'd like to use the same Database to store user information,such as chat history, user preferences, etc. that needs strict security guards. 
6. Order Placement: Yes. Also needs Shopping Assistant to use the user input in  chat, to place an order for the user, and ask confirmation before placing the order
7. Order Tracking: Yes
8. Wishlist/Favorites: Yes
9. Chatbot/Conversational UI: Yes, Yes, and Yes! Need a good UI for the application. 
10. Notifications: Not at this time. Maybe next version
11. Reviews & Ratings: Not at this time. 
12. Integration with Payment Gateways: Yes, only a mock up API for this version. This is an experiment project. It is a quick prototype. 
13. Customer Support: No. Hey, this online Agent is the customer support! Haha
14. Personalized Offers: Yes
15. Inventory Management (for sellers): Not at this time. Something that can be added in next iteration. 

**Agent**: 

Thank you for the detailed priorities and context! Here’s a refined list of the core capabilities to implement for your quick experimental online shopping assistant, based on your preferences:

1. Product Search
2. Product Recommendations
3. Shopping Cart Management
4. User Authentication (using a separate Azure PostgreSQL DB for auth, and the same DB for user info, chat history, preferences, with strict security)
5. Order Placement (via chat, with confirmation)
6. Order Tracking
7. Wishlist/Favorites
8. Chatbot/Conversational UI (with a strong, user-friendly UI)
9. Integration with Payment Gateways (mock API only)
10. Personalized Offers

Excluded for now: Price Comparison, Notifications, Reviews & Ratings, Customer Support, Inventory Management.

Next, I’ll document these prioritized capabilities in your project for easy reference and team alignment.