// src/App.tsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import LoginForm from './components/LoginForm';
import Feed from './components/Feed';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1>Социальная сеть</h1>
        </header>
        <main className="App-main">
          <Routes>
            <Route path="/" element={<LoginForm />} />
            <Route path="/feed" element={<Feed />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;