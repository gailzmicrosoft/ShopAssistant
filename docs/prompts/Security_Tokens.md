# Security Tokens in Shopping Assistant

This document explains how authentication tokens specifically Jason Web Tokens (JWTs) are used in the Shopping Assistant application, including how they are generated, what they contain, how they are used, and best practices for secure implementation.

---

## 1. How is the token generated?
- The token is generated by the FastAPI backend when a user successfully registers or signs in.
- The backend uses a secure library (e.g., PyJWT) to create a JWT, signing it with a secret key.
- The JWT contains encoded user information (claims), such as user ID, username, and an expiration time.

## 2. Which component generates it?
- The FastAPI backend is responsible for generating the token after verifying user credentials.
- The backend creates and returns the JWT to the frontend (web app) upon successful authentication.

## 3. What information does the token contain?
A typical JWT includes:
- `sub` (subject): the user’s unique ID
- `username` or `email`
- `exp`: expiration timestamp
- Optional: user roles, permissions, or other claims

**Example JWT payload:**
```json
{
  "sub": "12345",
  "username": "alex",
  "exp": 1715700000
}
```

## 4. How is it passed to the backend for each request?
- After sign-in/registration, the frontend stores the JWT (preferably in memory or a secure HTTP-only cookie).
- For each subsequent API request, the frontend includes the token in the HTTP Authorization header:
  ```
  Authorization: Bearer <JWT>
  ```
- The backend extracts and verifies the token on every request, authenticating the user and authorizing actions.

## 5. Best Practice Steps
1. **User registers or signs in.**
2. **Backend verifies credentials and generates a JWT** (using a strong secret, short expiration, and secure claims).
3. **Frontend receives and stores the JWT** (preferably in memory or a secure cookie).
4. **Frontend sends the JWT in the Authorization header** for every authenticated API request.
5. **Backend validates the JWT** on each request, extracts user info, and processes the request.
6. **On logout**, the frontend deletes the token (and, if using cookies, the backend can also blacklist tokens if needed).

## 6. Security Best Practices
- Use HTTPS for all communication.
- Use short-lived tokens and refresh tokens if needed.
- Store tokens securely (avoid localStorage for sensitive apps; prefer HTTP-only cookies or in-memory storage).
- Never expose your JWT secret.
- Validate the token signature and expiration on every request.

---

**Summary for this app:**
- FastAPI backend generates and signs the JWT.
- JWT contains user identity and session info.
- Frontend sends the JWT in the Authorization header for each request.
- Backend authenticates and authorizes using the token for every operation (orders, queries, etc.).
