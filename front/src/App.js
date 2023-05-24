import { BrowserRouter, Routes, Route } from 'react-router-dom';
import s from './App.module.scss';
import { Header } from './Components/Header/Header';
import { MainPage } from './Components/Pages/MainPage/MainPage';
import Navbar from './Components/Navbar/Navbar';
import { Dashboard } from './Components/Pages/Dashboard/Dashboard';

const App = () => {
  return (
    <div className={s.wrapper}>
      <BrowserRouter>
        <Header />
        <div className={s.content}>
          <Navbar />
          <Routes>
            <Route path="/" element={<MainPage/>} />
            <Route path="/dashboard" element={<Dashboard/>}/>
          </Routes>
        </div>
      </BrowserRouter>
    </div>
  );
}

export default App;
