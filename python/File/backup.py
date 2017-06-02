import shutil, os

os.chdir('E:\\')
print('Start backup...')
shutil.copytree('E:\\MyBook\\RecentRead\\Future\\iOS', 'E:\\iOS_Book_Backup')
print('Backup complete!')


