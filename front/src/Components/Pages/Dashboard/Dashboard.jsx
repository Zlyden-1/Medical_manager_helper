import React, { useState } from 'react'
import s from './Dashboard.module.scss'
import axios from 'axios';
import { NavLink } from 'react-router-dom';
import { useSelector} from 'react-redux';
import { LineDiagram } from '../../Diagram/LineDiagram/LineDiagram';
import { DoughnutDiagram } from '../../Diagram/DoughnutDiagram/DoughnutDiagram';
import { AiOutlineDown } from 'react-icons/ai'
import { HorizontalDiagram } from '../../Diagram/HorizontalDiagram/HorizontalDiagram';


export const Dashboard = () => {
	const data = useSelector(state => state.data);
	console.log(data);
	const [selectedPost, setSelectedPost] = useState([]);
	const [filter1Open, setFilter1Open] = useState(false);
	const toggleFilter1 = () => {
		setFilter1Open(filter1Open => !filter1Open);
	}
	const handleDownloadFile = () => {
		const url = "http://back:8000/api/diagnoses/download/";
		const filename = data['имя файла'];
		const queryAdress = url + filename;
		axios.get(queryAdress, { responseType: "blob" })
			.then(response => {
				const url = URL.createObjectURL(new Blob([response.data]));
				const link = document.createElement("a");
				link.href = url;
				link.download = "file.docx";
				document.body.appendChild(link);
				link.click();
				document.body.removeChild(link);
			})
			.catch(error => {
				console.log(error);
			});
	}
	const handlePostChange = (e) => {
		const post = e.target.value;
		if (e.target.checked) {
			setSelectedPost([...selectedPost, post]);
		} else {
			setSelectedPost(selectedPost.filter(p => p !== post));
		}
	};
	const allPost = data && data['данные'] ? data['данные'].map(item => item['Должность']) : [];
	const uniquePost = [...new Set(allPost)];
	const filteredData = data && data['данные'] ? data['данные'].filter(item => selectedPost.includes(item['Должность'])) : [];

	if (data) {
		return (
			<div className={s.wrapper}>
				<div className={s.wrapperfilter}>
					<div className={s.filter}>
						<div onClick={toggleFilter1}>Должность врача <AiOutlineDown className={s.icon} /></div>
						<div className={s.filterMenu}>
							{filter1Open
								? uniquePost.map(position => (
									<label className={s.label} key={position}>
										<input
											type="checkbox"
											className={s.input}
											value={position}
											onChange={handlePostChange}
										/>
										{position}
									</label>
								))
								: null}
						</div>
					</div>
					<div className={s.filter}>
						Медицинское учреждение <AiOutlineDown className={s.icon} />
					</div>
					<div className={s.filter}>
						Дата назначения <AiOutlineDown className={s.icon} />
					</div>
					<div className={s.filter}>
						Корректность назначения <AiOutlineDown className={s.icon} />
					</div>
				</div>
				<div className={s.separator}>
					<div className={s.wrapperleft}>
						<NavLink to='/table' className={s.buttonone}>
							Посмотреть таблицу с результатами анализа
						</NavLink>
						<button className={s.buttontwo} onClick={handleDownloadFile}>
							Скачать таблицу с результатами анализа
						</button>
						<div className={s.diagram}>
							<LineDiagram data={filteredData.length > 0 ? filteredData : data['данные']} />
						</div>
					</div>
					<div className={s.wrapperright}>
						<div className={s.diagram}>
							<DoughnutDiagram data={filteredData.length > 0 ? filteredData : data['данные']} />
						</div>
						<div className={s.diagram}>
							<HorizontalDiagram data={filteredData.length > 0 ? filteredData : data['данные']} />
						</div>
					</div>
				</div>
			</div>
		)
	}
	else {
		return (
			<div className={s.error}>
				Выберите файл для анализа на главной странице!
			</div>
		)
	}
}