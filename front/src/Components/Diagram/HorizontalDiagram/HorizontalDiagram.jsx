import React from 'react';
import {
	Chart as ChartJS,
	CategoryScale,
	LinearScale,
	BarElement,
	Title,
	Tooltip,
	Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);


export const HorizontalDiagram = (props) => {
	
	const options = {
		indexAxis: 'y',
		elements: {
			bar: {
				borderWidth: 2,
			},
		},
		responsive: true,
		plugins: {
			legend: {
				position: 'bottom',
			},
			title: {
				display: true,
				text: 'Три лучших врача',
				font: {
					size: 14
				}
			},
		},
	};

	const labels = [];

	const data = {
		labels,
		datasets: [
			{
				label: 'Соответствует стандарту',
				data: [],
				borderColor: 'rgba(54, 162, 235, 1)',
				backgroundColor: 'rgba(54, 162, 235, 0.5)',
			},
			{
				label: 'Доп. назначения',
				data: [],
				borderColor: 'rgba(255, 99, 132, 1)',
				backgroundColor: 'rgba(255, 99, 132, 0.5)',
			},
			{
				label: 'Недостаточные назначения',
				data: [],
				borderColor: 'rgba(255, 206, 86, 1)',
				backgroundColor: 'rgba(255, 206, 86, 0.5)',
			},
		],
	};
	return <Bar options={options} data={data} />;
}
