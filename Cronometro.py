import time
import os
h = min = seg = 0
while True:
    print('{}:{}:{}'.format(h,min,seg))
    time.sleep(1)
    seg += 1
    if seg == 60:
        seg = 0
        min += 1
    if min == 60:
        min = 0
        h += 1
    os.system('cls')