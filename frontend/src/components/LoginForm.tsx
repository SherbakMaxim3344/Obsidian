// src/components/LoginForm.tsx
import React, { useState } from 'react';

function LoginForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    
    try {
      const response = await fetch('http://localhost:8000/auth/login', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      if (response.ok) {
        localStorage.setItem('token', data.access_token);
        alert('Успешный вход!');
        window.location.href = '/feed';
      } else {
        alert('Ошибка: ' + (data.detail || 'Неверные данные'));
      }
    } catch (error) {
      console.error('Error:', error);
      alert('Сетевая ошибка');
    }
  };

  return (
    <div className="login-form">
      <h2>Вход</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <input
            type="text"
            placeholder="Логин"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="form-input"
            required
          />
        </div>
        <div className="form-group">
          <input
            type="password"
            placeholder="Пароль"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="form-input"
            required
          />
        </div>
        <button type="submit" className="submit-btn">
          Войти
        </button>
      </form>
      <p className="register-link">
        Нет аккаунта? <a href="/register">Зарегистрироваться</a>
      </p>
    </div>
  );
}

export default LoginForm;