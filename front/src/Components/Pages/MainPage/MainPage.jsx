import React, { useState } from 'react';
import axios from 'axios';
import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import s from './MainPage.module.scss';

export const MainPage = () => {
  const [file, setFile] = useState(null);
  const [name, setName] = useState("");
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleFileChange = e => {
    setFile(e.target.files[0]);
  }
  const handleNameChange = event => {
    setName(event.target.value);
  }
  const setData = (data) => {
    dispatch({ type: 'SET_MAIN_PAGE_DATA', payload: data });
    navigate('/dashboard');
  }
  const handleSubmit = async e => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('name', name);
    formData.append('file', file);

    try {
      const response = await axios.post('http://178.170.197.106/diagnoses/upload/protocols', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setData(response.data);

    } catch (error) {
      console.error(error.response);
      console.log(error.response);
    };
  }

  return (
    <div className={s.wrapper}>
      <form onSubmit={handleSubmit}>
        <div>Введите название отчета:</div>
        <input type="text" value={name} required onChange={handleNameChange} />
        <input type="file" title=" " required onChange={handleFileChange} accept='.xlsx' />
        <button type="submit">Загрузить файл</button>
      </form>
    </div>
  );
}