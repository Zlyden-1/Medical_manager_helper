import React, { useState } from 'react'
import s from './Dashboard.module.scss'
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { LineDiagram } from '../../Diagram/LineDiagram/LineDiagram';
import { DoughnutDiagram } from '../../Diagram/DoughnutDiagram/DoughnutDiagram';
import { AiOutlineDown } from 'react-icons/ai'



export const Dashboard = () => {
	const data = useSelector(state => state.data);
	const [selectedPost, setSelectedPost] = useState([]);
	const [filter1Open, setFilter1Open] = useState(false);
	const toggleFilter1 = () => {
		setFilter1Open(filter1Open => !filter1Open);
	}
	const allPost = data['данные'].map(item => item['Должность']);
	const uniquePost = [...new Set(allPost)];
	const handlePostChange = (e) => {
		const post = e.target.value;
		if (e.target.checked) {
			setSelectedPost([...selectedPost, post]);
		} else {
			setSelectedPost(selectedPost.filter(p => p !== post));
		}
	};
	const filteredData = data['данные'].filter(item => selectedPost.includes(item['Должность']));
	const result = Object.keys(filteredData).map((key) => [key, filteredData[key]]);

	return (
		<div className={s.wrapper}>
			<div className={s.wrapperfilter}>
				<div className={s.filter} onClick={toggleFilter1}>
					Должность врача <AiOutlineDown className={s.icon} />
				</div>
				<div className={s.filterMenu}>
					{filter1Open
						? uniquePost.map(position => (
							<label key={position}>
								<input
									type="checkbox"
									name="filterItem1"
									value={position}
									onChange={handlePostChange}
								/>
								{position}
							</label>
						))
						: null}
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
					<NavLink to='/table' className={s.button}>
						Посмотреть таблицу с результатами анализа
					</NavLink>
					<button className={s.button}>
						Скачать таблицу с результатами анализа
					</button>
					<div className={s.diagram}>
						<LineDiagram data={filteredData} />
					</div>
				</div>
				<div className={s.wrapperright}>
					<div className={s.diagram}>
						<DoughnutDiagram data={filteredData ? filteredData : data["данные"]} />
					</div>
				</div>
			</div>
		</div>
	)
}