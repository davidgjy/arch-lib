import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
print('Sheet names: %s' % wb.get_sheet_names())
sheet = wb.get_sheet_by_name('Sheet3')
print('Sheet3 name: %s' % sheet)
print('Sheet3 type: %s' % type(sheet))
print('Sheet3 title: %s' % sheet.title)
anotherSheet = wb.active
print('Active sheet: %s' % anotherSheet.title)

