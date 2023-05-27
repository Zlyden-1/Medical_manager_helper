import { BrowserRouter, Routes, Route } from 'react-router-dom';
import s from './App.module.scss';
import { Header } from './Components/Header/Header';
import { MainPage } from './Components/Pages/MainPage/MainPage';
import Navbar from './Components/Navbar/Navbar';
import { Dashboard } from './Components/Pages/Dashboard/Dashboard';
import { Table } from './Components/Pages/Table/Table';
import { Provider } from 'react-redux';
import store from './redux/main-reducer'

const App = () => {
  return (
    <div className={s.wrapper}>
      <BrowserRouter>
        <Provider store={store}>
          <Header />
          <div className={s.content}>
            <Navbar />
            <Routes>
              <Route path="/" element={<MainPage />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/table" element={<Table/>} />
            </Routes>
          </div>
        </Provider>
      </BrowserRouter>
    </div>
  );
}

export default App;
