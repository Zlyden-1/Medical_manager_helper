from datetime import datetime

import pytz

from ..database import retrieve_diagnosis_standard_by_name, add_rated_diagnosis, add_diagnosis_standard
from ..readers import xslx, pdf
from ..file_builders import word

tz = pytz.timezone('Europe/Moscow')
OK = 'Ок'
LACK = 'Недостаточные назначения'
OVERAGE = 'Избыточные назначения'


async def rate_prescriptions(name: str, file):
    data: list[dict] = xslx.reader(file)
    for diagnosis in data:
        diagnosis['Источник данных'] = name
        diagnosis['Дата загрузки'] = datetime.now(tz).date()
        standard = await retrieve_diagnosis_standard_by_name(diagnosis['Вазомоторный ринит'])
        diagnosis['Лишние назначения'] = []
        if diagnosis['Назначения'] == standard['Назначения']:
            diagnosis['Оценка'] = OK
        elif diagnosis['Назначения'] in standard['Назначения']:
            diagnosis['Оценка'] = LACK
        else:
            diagnosis['Оценка'] = OVERAGE
            for prescription in diagnosis['Назначения']:
                if prescription not in standard['Назначения']:
                    diagnosis['Лишние назначения'].append(prescription)
        await add_rated_diagnosis(diagnosis)
    filename = word.builder(name, data)
    return data, filename


async def add_standards(file):
    data = await pdf.reader(file)
    async for standard in data:
        await add_diagnosis_standard(standard)
    return True  # TODO: нужно ли возвращать новый список стандартов?
