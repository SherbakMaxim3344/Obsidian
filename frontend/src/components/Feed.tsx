// src/pages/Feed.tsx
import React, { useEffect, useState } from 'react';

function Feed() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    // Пример запроса с токеном
    const token = localStorage.getItem('token');
    if (!token) {
      window.location.href = '/';
      return;
    }
    
    // Здесь будешь получать посты
    console.log('Токен:', token);
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('token');
    window.location.href = '/';
  };

  return (
    <div>
      <h1>Лента</h1>
      <button onClick={handleLogout}>Выйти</button>
      <p>Здесь будут посты...</p>
    </div>
  );
}

export default Feed;