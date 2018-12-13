f = open("p059_cipher.txt", "r")
for line in f:
    s = str(line)
s = str(s)[:-1]
s = s.split(",")
s = [int(i) for i in s]


p = []
for a in range(97,123):
    for b in range(97,123):
        for c in range(97,123):
            row = []
            for i in range(0,len(s)-1,3):
                q = [chr(s[i]^a), chr(s[i+1]^b), chr(s[i+2]^c)]
                for j in q:
                    row.append(j)
            if bool(re.match("[ a-z-(]", "".join(row))):
                print(a,b,c)
                print(row[:10])
                p.append(row)
 
#103 111 100               
#['(', 'T', 'h', 'e', ' ', 'G', 'o', 's', 'p', 'e']

a = 103
b = 111
c = 100
row = []        
for i in range(0,len(s)-1,3):
    q = [s[i]^a, s[i+1]^b, s[i+2]^c]
    for j in q:
        row.append(j)

sum(row)+ord(46)
