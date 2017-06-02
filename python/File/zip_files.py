import zipfile

newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('Brief.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.write('a.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()


