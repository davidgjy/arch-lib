import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
print('Sheet1:A1: %s' % sheet['A1'])
print('Sheet1:A1 value: %s' % sheet['A1'].value)
c = sheet['B1']
print('Sheet1:B1 value: %s, coordinate: %s, row: %s, column: %s' % (c.value, c.coordinate, str(c.row), c.column))
