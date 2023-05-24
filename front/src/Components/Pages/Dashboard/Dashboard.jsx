import React from 'react'
import s from './Dashboard.module.scss'
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Doughnut } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend);

export const Dashboard = () => {
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
			<div className={s.diagram}>
				<Doughnut options={options} data={data} />
			</div>
		</div>
	)
}


const data = {
	labels: ['Соответствует стандарту', 'Доп. назначения', 'Недостаточные назначения'],
	datasets: [
		{
			label: '# of Votes',
			data: [12, 19, 3],
			backgroundColor: [
				'rgba(255, 99, 132, 0.2)',
				'rgba(54, 162, 235, 0.2)',
				'rgba(255, 206, 86, 0.2)',
			],
			borderColor: [
				'rgba(255, 99, 132, 1)',
				'rgba(54, 162, 235, 1)',
				'rgba(255, 206, 86, 1)',
			],
			borderWidth: 1,
		},
	],
};
const options = {
	maintainAspectRatio: false,
	plugins: {
		legend: {
		  position: "left"
		}
	}
};