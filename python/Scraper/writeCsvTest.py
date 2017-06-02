import csv
#from os import open

csvFile = open("files/test2.csv", 'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number plus 5', 'number times 5'))
    for i in range(10):
        writer.writerow( (i, i+5, i*5))
finally:
    csvFile.close()
