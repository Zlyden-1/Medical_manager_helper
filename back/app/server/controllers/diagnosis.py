from datetime import datetime

import pytz

from ..database import retrieve_diagnosis_standard_by_name, add_rated_diagnosis, add_diagnosis_standard
from ..readers import xslx, pdf
from ..file_builders import word

tz = pytz.timezone('Europe/Moscow')
OK = 0
LACK = 1
OVERAGE = 2


async def rate_prescriptions(name: str, file):
    data: list[dict] = xslx.reader(file)
    for diagnosis in data:
        diagnosis['protocol_name'] = name
        diagnosis['upload_date'] = datetime.now(tz).date()
        standard = await retrieve_diagnosis_standard_by_name(diagnosis['name'])
        diagnosis['extra_prescriptions'] = []
        if diagnosis['prescriptions'] == standard['prescriptions']:
            diagnosis['code'] = OK
        elif diagnosis['prescriptions'] in standard['prescriptions']:
            diagnosis['code'] = LACK
        else:
            diagnosis['code'] = OVERAGE
            for prescription in diagnosis['prescriptions']:
                if prescription not in standard['prescriptions']:
                    diagnosis['extra_prescriptions'].append(prescription)
        await add_rated_diagnosis(diagnosis)
    filename = word.builder(name, data)
    return data, filename


async def add_standards(file):
    data = await pdf.reader(file)
    async for standard in data:
        await add_diagnosis_standard(standard)
    return True  # TODO: нужно ли возвращать новый список стандартов?
