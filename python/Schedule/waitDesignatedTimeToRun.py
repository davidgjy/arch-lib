import time, datetime

startTime = datetime.datetime(2016, 6, 8, 16, 45, 0)
print('Program not starting yet...')
while datetime.datetime.now() < startTime:
	time.sleep(1)
print('Program now starts on %s' % startTime)
print('Executing...')
