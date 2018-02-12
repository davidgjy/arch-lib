import time
import datetime
import os

print('Scheduled cache cleaner started...')
while True:
    time.sleep(3600 * 24)
    print('Releasing cache...')
    os.system('echo 3 > /proc/sys/vm/drop_caches')
    print('Clean complete!')

