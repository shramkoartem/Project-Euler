f = open("p059_cipher.txt", "r")
for line in f:
    s = str(line)
s = str(s)[:-1]
s = s.split(",")
s = [int(i) for i in s]
x = [chr(i) for i in s]

