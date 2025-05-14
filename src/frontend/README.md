# ShopAssistant Frontend (React)

This folder contains the React web application for the ShopAssistant project. The frontend provides a modern, interactive user interface for registration, login, and chatting with the AI-powered shopping assistant.

---

## 🚀 Quick Start: Running the React App

1. **Install Node.js and npm**
   - Download and install Node.js (includes npm) from [nodejs.org](https://nodejs.org/).
   - Verify installation:
     ```pwsh
     node -v
     npm -v
     ```

2. **Install dependencies**
   - Open a terminal in this `frontend` folder:
     ```pwsh
     npm install
     ```

3. **Start the development server**
   - Run:
     ```pwsh
     npm start
     ```
   - The app will open in your browser at [http://localhost:3000](http://localhost:3000)

4. **Connect to the backend**
   - Make sure your FastAPI backend is running (see backend README for instructions).
   - The frontend expects the backend API (e.g., `/chat/message`) to be available. You may need to set up a proxy (see below).

---

## 📝 Project Structure

- `App.jsx` — Main entry point, handles authentication and routing.
- `SignInRegister.jsx` — Handles user registration and login.
- `ShopAssistant.jsx` — Chat interface for interacting with the assistant.

---

## 🔑 Key React Concepts

- **Component**: A reusable UI building block (e.g., `App`, `SignInRegister`, `ShopAssistant`).
- **State**: Data managed by a component (e.g., user info, chat messages).
- **Props**: Data passed from parent to child components.
- **Hooks**: Functions like `useState` and `useEffect` for managing state and side effects.
- **JSX**: A syntax extension for writing HTML-like code in JavaScript.

**Learn more:**
- [React Official Tutorial](https://react.dev/learn/tutorial-tic-tac-toe)
- [React Main Docs](https://react.dev/learn)
- [React Components & Props](https://react.dev/learn/your-first-component)
- [React State](https://react.dev/learn/state-a-components-memory)

---

## ⚙️ Proxying API Requests (Optional, for local dev)
If your backend runs on a different port (e.g., 8000), add a `proxy` field to your `package.json`:
```json
"proxy": "http://localhost:8000"
```
This lets you call `/chat/message` from the frontend without CORS issues.

---

## 🛠️ Useful npm Scripts
- `npm start` — Start the dev server
- `npm run build` — Build for production
- `npm test` — Run tests (if any)

---

## 💡 Tips for Learning React Fast
- Build small features and experiment with components and state.
- Use the React DevTools browser extension for debugging.
- Read the [React documentation](https://react.dev/learn) and try the interactive examples.
- Don’t worry about memorizing everything—focus on understanding how components, state, and props work together.

---

## 📚 More Resources
- [Codecademy: Learn React](https://www.codecademy.com/learn/react-101)
- [freeCodeCamp: React](https://www.freecodecamp.org/learn/front-end-development-libraries/react/)
- [React Patterns](https://reactpatterns.com/)

---

Happy coding! If you get stuck, check the docs above or ask for help.
