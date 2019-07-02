ndat=[]
for i in range(0,20):
    a = dat[0][i].replace(' ', '')
    ndat.append(a)

data = []
for i in range(0,20):  
    A = [int(ndat[i][j:j+2]) for j in range(0,40,2)]
    data.append(A)

def right(dataset):
    global res_right
    res_right = 1
    for row in range(0,20):
        for i in range(0,17):
            prod = dataset[row][i]*dataset[row][i+1]*dataset[row][i+2]*dataset[row][i+3]
            if prod > res_right:
                res_right = prod
    return res_right

def down(ds):
    global res_down
    res_down = 1
    for i in range(0,20):
        for row in range(0,17):
            prod = ds[row][i]*ds[row+1][i]*ds[row+2][i]*ds[row+3][i]
            if prod > res_down:
                res_down  = prod
    return res_down

def diag(ds):
    global res_diag, process
    res_diag = 1
    process = []
    for i in range(0,17):
        for j in range(0,17):
            prod = ds[i][j]*ds[i+1][j+1]*ds[i+2][j+2]*ds[i+3][j+3]
            process.append([ds[i][j],ds[i+1][j+1],ds[i+2][j+2],ds[i+3][j+3],'is',prod])
            if prod > res_diag:
                res_diag = prod
    return res_diag

