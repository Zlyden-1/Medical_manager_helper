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
	const positions = {};
	props.data.forEach((record) => {
	  const position = record["Должность"];
	  if (!positions[position]) {
		positions[position] = {
		  'Избыточные назначения': 0,
		  'Соответствует стандарту': 0,
		  'Недостаточные назначения': 0,
		};
	  }
  
	  positions[position][record["Оценка"]] += 1;
	});
  
	const sortedRatings = Object.entries(positions)
	  .sort((a, b) => {
		const aTotal = Object.values(a[1]).reduce((sum, count) => sum + count, 0);
		const bTotal = Object.values(b[1]).reduce((sum, count) => sum + count, 0);
		return bTotal - aTotal;
	  })
	  .slice(0, 3);
  
	const labels = sortedRatings.map((rating) => rating[0]);
  
	const data = {
	  labels,
	  datasets: [
		{
		  label: 'Соответствует стандарту',
		  data: sortedRatings.map((rating) => rating[1]['Соответствует стандарту']),
		  borderColor: 'rgba(54, 162, 235, 1)',
		  backgroundColor: 'rgba(54, 162, 235, 0.5)',
		},
		{
		  label: 'Доп. назначения',
		  data: sortedRatings.map((rating) => rating[1]['Избыточные назначения']),
		  borderColor: 'rgba(255, 99, 132, 1)',
		  backgroundColor: 'rgba(255, 99, 132, 0.5)',
		},
		{
		  label: 'Недостаточные назначения',
		  data: sortedRatings.map((rating) => rating[1]['Недостаточные назначения']),
		  borderColor: 'rgba(255, 206, 86, 1)',
		  backgroundColor: 'rgba(255, 206, 86, 0.5)',
		},
	  ],
	};
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
        text: 'Три худших врача',
        font: {
          size: 14
        }
      },
    },
  };
  return <Bar options={options} data={data} />;
}