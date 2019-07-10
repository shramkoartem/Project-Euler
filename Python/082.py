test = np.loadtxt("p082_matrix.txt", delimiter=",")

grid = test[:]

size = len(test)

# init
for i in range(size):
    sol.append(grid[i, size -1])
    
for i in range(size-2, -1, -1):
    sol[0] += grid[0, i]
    
    # top down
    for j in range(1, size):
        sol[j] = min(sol[j-1] + grid[j, i], sol[j] + grid[j, i])
    
    # buttom up
    for j in range(size-2, -1, -1):
        sol[j] = min(sol[j], sol[j+1] + grid[j,i])
        
min(sol)
