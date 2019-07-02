def rect(h,v):
    n = h*v*(h-1)*(v-1)/4
    return n

for x in range(40,50):
    for y in range(70,60,-1):
        if rect(x,y) > 1950000 and rect(x,y) < 2000000:
            print(x,y,rect(x,y))
