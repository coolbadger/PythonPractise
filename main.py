#coding=utf-8
#求素数算法
import time
timeStart = time.time()
__author__ = 'badger'
NumCount = 0
startNum = 2L
endNum = 100000L
message = str(startNum) + '到' + str(endNum) + '内素数：\n'
print(message)

for i in xrange(startNum, endNum - 1L, 1L):
    count = 0L
    for n in xrange(2L, i, 1L):
        if(i % n == 0):
            count += 1L
            break
    if(count == 0):
        NumCount += 1L
        message = '第' + str(NumCount) + '个:' + str(i)
        print(message)
timeEnd = time.time()

print('耗时：' + str(timeEnd - timeStart) + '秒')

