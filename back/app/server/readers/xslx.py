import re

import pandas as pd


def reader(file):
    data = pd.read_excel(file).to_dict('records')
    for diagnosis in data:
        diagnosis['Назначения'] = [i for i in re.split(r'\n+', diagnosis['Назначения']) if i]
    return data


if __name__ == '__main__':
    with open('../media/Dataset.xlsx', 'rb') as file:
        print(reader(file))
