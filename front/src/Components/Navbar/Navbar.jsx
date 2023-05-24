import React, { useState } from 'react';
import './Navbar.css';

const Navbar = () => {
  const [navbarOpen, setNavbarOpen] = useState(false);

  const toggleNavbar = () => {
    setNavbarOpen(!navbarOpen);
  }

  const closeNavbar = () => {
    setNavbarOpen(false);
  }

  return (
    <nav className="navbar">
      <button className="navbar-toggle" onClick={toggleNavbar}>
        <span className="navbar-toggle-icon">&#9776;</span>
      </button>
      <ul className={`navbar-list ${navbarOpen ? 'navbar-list-open' : ''}`}>
        <li className="navbar-item"><a href="#">Home</a></li>
        <li className="navbar-item"><a href="#">About</a></li>
        <li className="navbar-item"><a href="#">Contact</a></li>
      </ul>
      {navbarOpen && <div className="navbar-overlay" onClick={closeNavbar}></div>}
    </nav>
  );
}

export default Navbar;