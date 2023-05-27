import React from 'react'
import s from './Table.module.scss'
import { useSelector } from 'react-redux';

export const Table = () => {
	const data = useSelector(state => state.data);
	if (data) {
		return (
			<div className={s.wrapper}>
				<table className={s.table}>
					<thead>
						<tr>
							{Object.keys(data["данные"][0]).map((key) => {
								if (key === "Лишние назначения") {
									return null; // если ключ содержит "Лишние назначения", то пропускаем его
								}
								else {
									return <th key={key}>{key}</th>
								}
							})}
						</tr>
					</thead>
					<tbody>
						{data["данные"].map((dataItem, index) => {
							const isExcess = dataItem["Лишние назначения"] !== "";
							const additionalText = isExcess ? "<br><span style='color:red'>" + dataItem["Лишние назначения"] + "</span>" : "";
							return (
								<tr key={index}>
									{Object.keys(dataItem).map((key, index) => {// используем Object.keys, чтобы получить список ключей объекта
										const value = dataItem[key];
										if (key === "Лишние назначения") {
											return null; // если ключ содержит "Лишние назначения", то пропускаем его
										} else if (Array.isArray(value)) {
											const text = value.join(",<br>") + additionalText;
											return <td className={s.rows} key={index} dangerouslySetInnerHTML={{ __html: text }} />;
										} else {
											return <td className={s.rows} key={index}>{value}</td>;
										}
									})}
								</tr>
							);
						})}
					</tbody>
				</table>
			</div>
		);
	}
}
