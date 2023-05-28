import React from 'react'
import { Chart as ChartJS, ArcElement, Tooltip, Legend, Title } from 'chart.js';
import { Doughnut } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend, Title)


export const DoughnutDiagram = (props) => {
	const rates = Array.isArray(props.data) ? props.data.map(i => i["Оценка"]) : [];
	const countOk= rates.reduce((total, rate) => (rate === 'Ок' ? total + 1 : total), 0);
	const countLack= rates.reduce((total, rate) => (rate === 'Недостаточные назначения' ? total + 1 : total), 0);
	const countOver= rates.reduce((total, rate) => (rate === 'Избыточные назначения' ? total + 1 : total), 0);
	
	const data = {
		labels: ['Соответствует стандарту', 'Доп. назначения', 'Недостаточные назначения'],
		datasets: [
			{
				label: '# of Votes',
				data: [countOk, countOver, countLack],
				backgroundColor: [
					'rgba(54, 162, 235, 0.2)',
					'rgba(255, 99, 132, 0.2)',
					'rgba(255, 206, 86, 0.2)',
				],
				borderColor: [		
					'rgba(54, 162, 235, 1)',
					'rgba(255, 99, 132, 1)',
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
				position: "left",
				labels: {
					usePointStyle: true //for style circle
				}
			},
			title: {
                display: true,
                text: 'Диаграмма корректности диагнозов',
                font:{
                    size: 16
                }
            },
		}
	};
	return <Doughnut options={options} data={data} />
} 
