#path = ...

txt = open(path+"p067_triangle.txt")

lines = txt.read().split('\n')

for i in range(len(lines)):
    lines[i] = lines[i].split(" ")
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j][0] == 0:
            lines[i][j][0] = lines[i][j][1]
        lines[i][j] = int(lines[i][j])

#function sums rows buttom -> up

def step(df):
    d = df[:]
    for row in range(len(d)-1,0,-1):
        for i in range(len(d[row])-1):
            a = d[row][i]
            b = d[row][i+1]
            d[row-1][i] = d[row-1][i] + max(a,b)
    return d
 
ans = step(lines)
ans
