import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
print(wb.get_sheet_names())

sheet = wb.get_sheet_by_name('Sheet3')
print(sheet.title)

sheet = wb.get_sheet_by_name('Sheet1')
print(sheet['A1'].value)
c = sheet['B1']
print(c.value)
print('Row ' + str(c.row) + ', Column ' + c.column + ' is ' + c.value)
print('Cell ' + c.coordinate + ' is ' + c.value)
print(sheet['C1'].value)


