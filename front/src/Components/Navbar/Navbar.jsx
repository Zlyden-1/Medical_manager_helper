import React, { useState } from 'react';
import s from './Navbar.module.scss';
import { NavLink } from 'react-router-dom';
import { RxHamburgerMenu } from 'react-icons/rx';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
	 <div className={s.wrapper}>
        <RxHamburgerMenu size="10px" className={s.burger} onClick={toggleMenu}/>
        <div className={`${s.menuItems} ${isOpen ? s.open : s.closed}`}>
          <NavLink to="/" className={s.pointer}>
            Главная
          </NavLink>
          <NavLink to="/dashboard" className={s.pointer}>
            Анализ
          </NavLink>
          <NavLink to="/standarts" className={s.pointer}>
            Стандарты
          </NavLink>
        </div>
    </div>
  );
};

export default Navbar;