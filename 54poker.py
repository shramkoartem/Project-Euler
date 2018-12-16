f = open("p054_poker.txt", "r")
cards = []
for row in f:
    cards.append(row)
    
cards = [i[:-1] for i in cards]
cards = [i.split(" ") for i in cards]
cards = [[[j[0],j[1]] for j in i]  for i in cards]
for row in cards:
    for c in row:
        if c[0] == "T":
            c[0] = c[0].replace("T","10")
        if c[0] == "J":
            c[0] = c[0].replace("J","20") 
        if c[0] == "Q":
            c[0] = c[0].replace("Q","30")            
        if c[0] == "K":
            c[0] = c[0].replace("K","40")  
        if c[0] == "A":
            c[0] =  c[0].replace("A","50")  
        c[0] = int(c[0])

cards = [[i[:5],i[5:]] for i in cards]


high_card = 1 
one_pair = 2
two_pairs = 3
three = 4
straight = 5
flush = 6
full_house = 7
four = 8
straight_flush = 9
royal_flush = 10

