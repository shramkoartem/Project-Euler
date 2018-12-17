f = open("p079_keylog.txt", "r")
logs = []
for row in f:
    logs.append(row[:-1])
    
digits = []
for row in logs:
    for i in row:
        if i not in digits:
            digits.append(i)
