#not optimal, need to break it after 73682
count = 8
for pound in range(0,2):
    for fifty in range(0,4):
        for twenty in range(0,10):
            if pound>0 and twenty >5:
                break
            for ten in range(0,20):
                if twenty>5 and ten > 10:
                    break
                for five in range(40):
                    if ten > 10 and five > 20:
                        break
                    for two in range(100):
                        if five > 20 and two > 50:
                            break
                        for one in range(200):
                            if two > 50 and one > 100:
                                break
                            s = pound*100 + fifty*50 + twenty*20 + ten*10 + five*5 + two*2 + one*1 
                            if s == 200:
                                count += 1
                                print(count)
