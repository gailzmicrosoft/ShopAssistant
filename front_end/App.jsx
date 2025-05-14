import React, { useState } from "react";
import SignInRegister from "./SignInRegister";
import ShopAssistant from "./ShopAssistant";

export default function App() {
  const [token, setToken] = useState(null);
  const [user, setUser] = useState(null);

  // Handles login/register and stores token
  const handleAuth = (userInfo, jwt) => {
    setUser(userInfo);
    setToken(jwt);
  };

  // Handles logout
  const handleLogout = () => {
    setUser(null);
    setToken(null);
  };

  return (
    <div>
      {!token ? (
        <SignInRegister onAuth={handleAuth} />
      ) : (
        <ShopAssistant user={user} token={token} onLogout={handleLogout} />
      )}
    </div>
  );
}
