
import numpy as np
dat = np.loadtxt('names.txt', delimiter=',', dtype=str)

for i in dat:
    i.strip('""')
res = [i.strip('"') for i in dat]

nam = sorted(res)
nam

names = [list(i) for i in nam]

import string

ans = names.copy()
answer = 0
result = []
for element in range(0,len(ans)):
    length = 0
    num = []
    for letter in ans[element]:
        pos = string.ascii_uppercase.index(letter)+1
        length += pos
        num.append(pos)
    answer += length*(element+1)
    result.append([element,num])    
