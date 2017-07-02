import time
import datetime
import os

print('Started...')
while True:
    time.sleep(5 * 3)
    print('Releasing cash...')
    os.system('echo 3 > /proc/sys/vm/drop_caches')
    print('Clean complete!')

