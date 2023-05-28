import React from "react";
import s from './Header.module.scss'
import { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";

export const Header = () => {
    const [pageTitle, setPageTitle] = useState('');
    const location = useLocation();
    useEffect(() => {
        switch (location.pathname) {
            case '/':
                setPageTitle('Загрузить файл для анализа');
                break;
            case '/dashboard':
                setPageTitle('Дашборды');
                break;
            case '/table':
                setPageTitle('Таблица с результатами');
                break;
            case '/standarts':
                setPageTitle('Стандартные назначения');
                break;
            default:
                setPageTitle('Загрузить файл для анализа');
        }
    }, [location]);
    return (

        <div className={s.wrapper}>
            <div className={s.header}>
                <img src="https://www.mos.ru/upload/structure/institutions/icon/dzm-01-no-text.png" alt="logo" />
                <div className={s.menu}>
                    {pageTitle}
                </div>
            </div>
        </div>
    )
}