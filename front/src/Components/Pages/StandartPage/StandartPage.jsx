import React, { useState } from 'react';
import axios from 'axios';
import s from './StandartPage.module.scss';

export const StandartPage = () => {
  const [file, setFile] = useState(null);
  const [diagnosis, setDiagnosis] = useState("");
  const [direction, setDirection] = useState("");
  const [age, setAge] = useState("");
  const [standart, setStandart] = useState("");
  const [data, setData] = useState([]);

  const handleFileChange = e => {
    setFile(e.target.files[0]);
  }
  const handleDiagnosisChange = event => {
    setDiagnosis(event.target.value);
  }
  const handleDirectionChange = event => {
    setDirection(event.target.value);
  }
  const handleAgeChange = event => {
    setAge(event.target.value);
  }
  const handleStandartChange = event => {
    setStandart(event.target.value);
  }
  const handleSubmit = async e => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('diagnosis', diagnosis);
    formData.append('direction', direction);
    formData.append('age', age);
    formData.append('standart', standart);
    formData.append('file', file);

    try {
      const response = await axios.post('http://178.170.197.106:8000/diagnoses/upload/standarts', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      console.log(response);
      setData(response.data);

    } catch (error) {
      console.error(error.response);
      console.log(error.response);
    };
  }

  return (
    <div className={s.wrapper}>
      <div className={s.title}>
        Выгруженные стандарты:
        <div>Стандарт1</div>
        <div>Стандарт2</div>
        <div>Стандарт3</div>
        <div>Стандарт4</div>
      </div>
      <form onSubmit={handleSubmit}>
      <div className={s.title}>Добавление стандарта:</div>
        <div className={s.beginform}>Диагноз:</div>
        <input type="text" value={diagnosis} required onChange={handleDiagnosisChange} />
        <div>Направление:</div>
        <input type="text" value={direction} required onChange={handleDirectionChange} />
        <div>Возраст:</div>
        <input type="text" value={age} required onChange={handleAgeChange} />
        <div>Стандарт:</div>
        <input type="text" value={standart} required onChange={handleStandartChange} />
        <input type="file" title=" " required onChange={handleFileChange} accept='.xlsx' />
        <button type="submit">Выгрузить стандарт</button>
      </form>
    </div>
  );
}