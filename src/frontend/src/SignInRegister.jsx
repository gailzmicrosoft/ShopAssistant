import React, { useState } from "react";

export default function SignInRegister({ onAuth }) {
  const [isRegister, setIsRegister] = useState(false);
  const [form, setForm] = useState({ username: "", email: "", password: "" });
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    // MOCK: Simulate successful login/register without backend
    setTimeout(() => {
      const mockUser = { id: 1, username: form.username, email: form.email };
      const mockToken = "mock-jwt-token";
      onAuth(mockUser, mockToken);
    }, 500);
  };

  return (
    <div className="auth-container">
      <h2>{isRegister ? "Register" : "Sign In"}</h2>
      <form onSubmit={handleSubmit}>
        <input
          name="username"
          placeholder="Username"
          value={form.username}
          onChange={handleChange}
          required
        />
        {isRegister && (
          <input
            name="email"
            placeholder="Email"
            value={form.email}
            onChange={handleChange}
            required
          />
        )}
        <input
          name="password"
          type="password"
          placeholder="Password"
          value={form.password}
          onChange={handleChange}
          required
        />
        <button type="submit">{isRegister ? "Register" : "Sign In"}</button>
      </form>
      <button onClick={() => setIsRegister((r) => !r)}>
        {isRegister ? "Already have an account? Sign In" : "New user? Register"}
      </button>
      {error && <div className="error">{error}</div>}
    </div>
  );
}
