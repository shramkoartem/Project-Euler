import math

#getting and adjusting data
f = open('1.txt', 'r')

nums = []
for line in f:
    nums.append(line)
    
nums= [i.split(',') for i in nums]

for i in nums:
    i[1] = i[1][:-1]
    
nums = [[int(i) for i in j] for j in nums]

#new list with pow*log(x) and row number
res = []
for line in range(0,len(nums)):
    
    slot = nums[line]
    a = line
    b = slot[1]*math.log(slot[0])
    res.append([a,b])

#sort the new list by the highest value
res.sort(key= lambda x: x[1], reverse = True)

#answer
res[0][0]+1
