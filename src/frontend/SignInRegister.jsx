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
    const endpoint = isRegister ? "/user/register" : "/user/login";
    try {
      const res = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });
      if (!res.ok) throw new Error("Authentication failed");
      const data = await res.json();
      // Assume backend returns { user, token }
      onAuth(data.user, data.token);
    } catch (err) {
      setError(err.message);
    }
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
