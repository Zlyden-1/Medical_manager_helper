import React from 'react';
import s from './Navbar.module.scss';
import {NavLink} from 'react-router-dom'
import { RxHamburgerMenu } from "react-icons/rx";

const Navbar = () => {
  return (
    <div className={s.wrapper}>  
        <RxHamburgerMenu className={s.burger}/>
        <NavLink to='/'className={s.pointer}>Главная</NavLink>
        <NavLink to='/dashboard'className={s.pointer}>Анализ</NavLink>
        <NavLink to='/'className={s.pointer}>Стандарты</NavLink>
    </div>
  );
}

export default Navbar;