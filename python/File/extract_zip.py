import zipfile, os

os.chdir('E:\\MyTest') # move to the folder with example.zip

exampleZip = zipfile.ZipFile('iOS7inAction_SourceCode.zip')
exampleZip.extractall('iOS7Code')
exampleZip.close()

