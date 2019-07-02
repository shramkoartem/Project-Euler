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

class Hand():
    
    def f_high_card(self,hand):
        m = 0
        for card in hand:
            if card[0] > m:
                m = card[0]
        return m
    
    def __init__(self, hand):
        self.hand = hand
        self.high_card = self.f_high_card(hand)
        self.score = 1
    
    def f_same_kind(self):
        vals = [i[0] for i in self.hand]
        v = set(vals)

        cards = []
        for i in v:
                c = 0
                for j in vals:
                    if j == i:
                        c += 1
                cards.append(c)
        if 4 in cards:
            return four
        if 3 in cards:
            if 2 in cards:
                return full_house
            else:
                return three
        if 2 in cards:
            if len(set(cards)) < len(cards):
                return two_pairs
            else: return pair
        return high_card
    
    def f_straight(self):
        vals = [i[0] for i in self.hand]
        suit = [i[1] for i in self.hand]
        vals.sort()
        if len(set(vals)) == len(vals):
            ans = []
            for i in range(0,4):
                if vals[i]+1 != vals[i+1]:
                    return 0
            if len(set(suit)) == 1:
                if vals[0] == 11:
                    return royal_flush
                else: return straight_flush
            else:
                return straight
        else: return 0
    
    def f_flush(self):
        suit = [i[1] for i in self.hand]
        if len(set(suit)) == 1:
            return flush
        else: return 0
        
    def evaluate(self):
        res = []
        a = self.f_same_kind()
        b = self.f_straight()
        c = self.f_flush()
        
        res.append(a)
        res.append(b)
        res.append(c)
        self.score = max(res)
    
    
count = 0
for row in cards:
    p1 = Hand(row[0])
    p2 = Hand(row[1])
    p1.evaluate()
    p2.evaluate()
    if p1.score == p2.score:
        if p1.high_card > p2.high_card:
            count += 1
            continue
    if p1.score > p2.score:
        count += 1
    
print(count)
