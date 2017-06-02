import PyPDF2

pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print('Pdf page number: %s' % pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print('First Page Text: %s' % pageObj.extractText())

