from openpyexcel import load_workbook


def reader(file):
    contents = await file.read()
    wb = load_workbook(filename=None, data=contents, read_only=True, data_only=True)
    return {}
