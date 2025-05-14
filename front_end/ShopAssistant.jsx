import React, { useState } from "react";

export default function ShopAssistant({ user, token, onLogout }) {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleInputChange = (e) => setInput(e.target.value);

  const handleSend = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;
    setLoading(true);
    // Add user message to chat
    setMessages((msgs) => [...msgs, { sender: "user", text: input }]);
    try {
      const response = await fetch("/chat/message", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ user_id: user.id, message: input, context: {} }),
      });
      const data = await response.json();
      setMessages((msgs) => [
        ...msgs,
        { sender: "assistant", text: data.response }
      ]);
    } catch (err) {
      setMessages((msgs) => [
        ...msgs,
        { sender: "assistant", text: "Sorry, there was an error." }
      ]);
    }
    setInput("");
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 600, margin: "2rem auto", padding: 20, border: "1px solid #ccc", borderRadius: 8 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <h2>Shopping Assistant</h2>
        <button onClick={onLogout}>Logout</button>
      </div>
      <div style={{ minHeight: 200, background: "#f9f9f9", padding: 10, borderRadius: 4, marginBottom: 16 }}>
        {messages.length === 0 && <div style={{ color: "#888" }}>Start chatting with your assistant!</div>}
        {messages.map((msg, idx) => (
          <div key={idx} style={{ textAlign: msg.sender === "user" ? "right" : "left", margin: "8px 0" }}>
            <span style={{ fontWeight: msg.sender === "user" ? "bold" : "normal" }}>
              {msg.sender === "user" ? "You" : "Assistant"}:
            </span> {msg.text}
          </div>
        ))}
      </div>
      <form onSubmit={handleSend} style={{ display: "flex", gap: 8 }}>
        <input
          type="text"
          value={input}
          onChange={handleInputChange}
          placeholder="Type your message..."
          style={{ flex: 1, padding: 8 }}
          disabled={loading}
        />
        <button type="submit" disabled={loading || !input.trim()}>
          {loading ? "Sending..." : "Send"}
        </button>
      </form>
    </div>
  );
}
