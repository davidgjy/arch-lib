import time

# record time of a procedure takes
startTime = time.time()
product = 1
for i in range(1, 50000):
    product = product * i
endTime = time.time()
print('The result is %s digits long.' % (len(str(product))))
print('Took %s seconds to calculate.' % round(endTime - startTime, 2))

