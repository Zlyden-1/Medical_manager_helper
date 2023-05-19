from ..database import retrieve_diagnosis_by_name

OK = 0
LACK = 1
OVERAGE = 2


async def rate_prescriptions(data: list[dict]):
    for diagnosis in data:
        standard = await retrieve_diagnosis_by_name(diagnosis['name'])
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
    return data
