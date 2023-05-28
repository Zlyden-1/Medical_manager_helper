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
									return null;
								}
								else if (key === "ID пациента") {
									key="ID"
									return <th key={key}>{key}</th>
								}
								else {
									return <th key={key}>{key}</th>
								}
							})}
						</tr>
					</thead>
					<tbody>
						{data["данные"].map((dataRow, index) => {
							const lackStyle = { background: "#FFE6AA" };
							const excessStyle = { background: "#FFB1C1" };
							const isExcess = dataRow["Оценка"] === "Избыточные назначения";
							const isLack = dataRow["Оценка"] === "Недостаточные назначения";
							const additionalText = isExcess ? `<br><span style='color:white;font-weight:bold;background-color:red'>${dataRow["Лишние назначения"]}</span>` : "";
							const style = isExcess ? excessStyle : (isLack ? lackStyle : { background: "#9AD0F5" });

							return (
								<tr key={`row_${index}`} style={style}>
									{Object.keys(dataRow).map((key, index) => {
										const value = dataRow[key];
										if (key === "Лишние назначения") {
											return null;
										} else if (Array.isArray(value)) {
											const text = `${value.join(",<br>")}${additionalText}`;
											return <td key={`cell_${index}`} dangerouslySetInnerHTML={{ __html: text }} />;
										} else if (key === "Источник данных"){
											return <td key={`cell_${index}`} style={{wordBreak:"break-word"}}>{value}</td>;
										}
										else {
											return <td key={`cell_${index}`}>{value}</td>;
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
