import React, { useState } from 'react';
import axios from 'axios';

export const MainPage = () => {
  const [file, setFile] = useState(null);
  const [data, setData] = useState(null);

  const handleFileChange = e => {
    setFile(e.target.files[0]);
  }

  const handleSubmit = async e => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('file', file, file.name);

    try {
      const response = await axios.post('http://178.170.197.106/upload/protocols', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      setData(response.data);
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} accept='.xlsx'/>
        <button type="submit">Загрузить файл</button>
      </form>
      {data && (
        <div>
          <h2>Данные из файла:</h2>
          <ul>
            {data.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
