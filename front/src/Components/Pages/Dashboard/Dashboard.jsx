import React from 'react'
import s from './Dashboard.module.scss'
import { NavLink } from 'react-router-dom';
import { LineDiagram } from '../../Diagram/LineDiagram/LineDiagram';
import { DoughnutDiagram } from '../../Diagram/DoughnutDiagram/DoughnutDiagram';

export const Dashboard = (props) => {
	console.log(props);
	return (
		<div className={s.wrapper}>
			<div className={s.wrapperfilter}>
				<div className={s.filter}>
					Должность врача
				</div>
				<div className={s.filter}>
					Медицинское учреждение
				</div>
				<div className={s.filter}>
					Дата назначения
				</div>
				<div className={s.filter}>
					Корректность назначения
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
						<LineDiagram data={props}/>
					</div>
				</div>
				<div className={s.wrapperright}>
					<div className={s.diagram}>
						<DoughnutDiagram data={props}/>
					</div>
				</div>
			</div>
		</div>
	)
}