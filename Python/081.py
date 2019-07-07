test = np.loadtxt("p081_matrix.txt", delimiter=",")

for i in range(78, -1, -1):
    test[79, i] += test[79, i+1]
    test[i, 79] += test[i+1, 79]
    
for i in range(78, -1, -1):
    for j in range(78, -1, -1):
        print("{} {}".format(i, j))
        test[i,j] += min(test[i+1,j],test[i,j+1])
