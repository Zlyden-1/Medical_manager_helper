import React from 'react'
import s from './LineDiagram.module.scss'
import { Chart as ChartJS, ArcElement, Tooltip, Legend, CategoryScale, LinearScale, PointElement, LineElement, Title } from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(ArcElement, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

export const LineDiagram = (props) => {
    const dates = [... new Set(Array.isArray(props.data) ? props.data.map(i => i["Дата оказания услуги"]) : [])];
    const datasets = [
        {
            label: 'Соответствует стандарту',
            data: [],
            borderColor: 'rgb(255, 99, 132)',
            backgroundColor: 'rgba(255, 99, 132, 0.5)',
        },
        {
            label: 'Доп. назначения',
            data: [],
            borderColor: 'rgb(53, 162, 235)',
            backgroundColor: 'rgba(53, 162, 235, 0.5)',

        },
        {
            label: 'Недостаточные назначения',
            data: [],
            borderColor: 'rgb(36, 212, 52)',
            backgroundColor: 'rgba(36, 212, 52, 0.5)',

        },
    ]
    for (let i = 0; i < dates.length; i++) {
        const currentDiagnoses = [];
        for (let j = 0; j < props.data.length; j++) {
            if (props.data[j]["Дата оказания услуги"] == dates[i]) {
                currentDiagnoses.push(props.data[j]["Оценка"])
            }
        }
        const countOk = currentDiagnoses.reduce((total, rate) => (rate === 'Ок' ? total + 1 : total), 0);
        const countLack = currentDiagnoses.reduce((total, rate) => (rate === 'Недостаточные назначения' ? total + 1 : total), 0);
        const countOver = currentDiagnoses.reduce((total, rate) => (rate === 'Избыточные назначения' ? total + 1 : total), 0);
        datasets[0].data.push(countOk);
        datasets[1].data.push(countLack);
        datasets[2].data.push(countOver);
    }

    const options = {
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

    const labels = dates;
    const data = {
        labels: labels,
        datasets: datasets
    }
    return <Line options={options} data={data} />;
}