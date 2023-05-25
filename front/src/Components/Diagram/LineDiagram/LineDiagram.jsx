import React from 'react'
import s from './LineDiagram.module.scss'
import { Chart as ChartJS, ArcElement, Tooltip, Legend, CategoryScale, LinearScale, PointElement, LineElement, Title } from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(ArcElement, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

export const options = {
    responsive: true,
    plugins: {
        legend: {
            position: 'bottom',
            labels: {
                usePointStyle: true
            }
        },
        title: {
            display: true,
            text: 'Chart.js Line Chart',
        },
    },
};

const labels = ['January', 'February', 'March', 'April'];

export const data = {
    labels,
    datasets: [
        {
            label: 'Соответствует стандарту',
            data: [4, 6, 8, 10],
            borderColor: 'rgb(255, 99, 132)',
            backgroundColor: 'rgba(255, 99, 132, 0.5)',
        },
        {
            label: 'Доп. назначения',
            data: [10, 22, 9, 0],
            borderColor: 'rgb(53, 162, 235)',
            backgroundColor: 'rgba(53, 162, 235, 0.5)',

        },
        {
            label: 'Недостаточные назначения',
            data: [6, 20, 14, 2],
            borderColor: 'rgb(36, 212, 52)',
            backgroundColor: 'rgba(36, 212, 52, 0.5)',

        },
    ],
};

export const LineDiagram = (props) => {
    return <Line options={options} data={data} />;
}