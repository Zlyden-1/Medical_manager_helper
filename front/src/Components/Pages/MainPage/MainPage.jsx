import React, { useState } from 'react';
import axios from 'axios';
import { Dashboard } from '../Dashboard/Dashboard';

export const MainPage = () => {
	const [file, setFile] = useState(null);
	const [name, setName] = useState("");
	const [data, setData] = useState("");

	const handleFileChange = e => {
		setFile(e.target.files[0]);
	}
	const handleNameChange = event => {
		setName(event.target.value);
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
			console.error(error.response.data);
			console.log(error.response.data.detail);
		}
		return <Dashboard data={data} />;
	}

	return (
		<div>
			<form onSubmit={handleSubmit}>
				<input type="text" value={name} onChange={handleNameChange} />
				<input type="file" onChange={handleFileChange} accept='.xlsx' />
				<button type="submit">Загрузить файл</button>
			</form>
			{data && (
				<div>
					<h2>Данные из файла:</h2>
					<ul>
						<div>
							{Object.keys(data["данные"][0]).map((key) => (
								<div>{key}</div>
							))}
						</div>
					</ul>
				</div>
			)}
		</div>
	);
}
