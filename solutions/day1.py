from collections import Counter
from helper.submit.submit import *
from utils import read_file_int

DAY = 1
setup(DAY)
file = read_file_int(DAY)

##################################################

ans = 0
prev = file[0]
for i in range(1, len(file)):
    if file[i] > prev:
        ans += 1
    prev = file[i]

submit(1, ans)

##################################################

ans = 0
prev = sum(file[0:3])
for i in range(1, len(file)-2):
    su = sum(file[i:i+3])
    if su > prev:
        ans += 1
    prev = su

submit(2, ans)
