// src/Login.js
import React, { useState } from 'react';
import styles from './login.module.css';
import { useNavigate } from 'react-router-dom';
import Admin from './Admin.js';

const Login = () => {
  const navigate = useNavigate();

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      const response = await fetch('http://localhost:3001/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        // Handle successful login, e.g., redirect to the next page
        navigate('/Admin');
        alert("logged in as admin");
      } else {
        // Handle invalid credentials
        alert("Invalid");
      }
    } catch (error) {
      console.error('Error during login:', error);
    }
  };


  return (
    <div className={styles.loginContainer}>
      <h2>Admin Login</h2>
      <form className={styles.form}>
        <label>
          Username:  
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </label>
        <label>
          Password:
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
        <button type="button" onClick={handleLogin}>
          Login
        </button>
      </form>
    </div>
  );
};

export default Login;
