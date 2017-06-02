import time, datetime

startTime = datetime.datetime(2016, 7, 29, 15, 45, 0)
print('Wait time to execute...')
while datetime.datetime.now() < startTime:
	time.sleep(1)
	
print('Program now starting!')
