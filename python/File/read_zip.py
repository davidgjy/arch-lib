import zipfile, os

# move to the folder with example.zip
os.chdir('E:\\MyBook\\RecentRead\\Future\\iOS') 
exampleZip = zipfile.ZipFile('iOS7inAction_SourceCode.zip')
for nameFile in exampleZip.namelist():
	print(nameFile)


