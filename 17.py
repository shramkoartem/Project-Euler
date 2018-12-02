def main(number):
    #value = int(input("\nPlease enter a positive integer < 1000000000 : "))
    global length, nums 
    length = 0
    nums = []
    for value in range(1,number):
        if value < 100:
            #print(processDigit(value))
            num = str(processDigit(value))
            num = num.replace(' ','')
        elif value > 100:
            #print(intName(value))
            num = str(intName(value))
            num = num.replace(' ','') 
        length += len(str(num))
        nums.append(str(num))
    return length

# turns a number into its English name
def intName(number):
    part = number
    nameMillion = ""
    nameThousand = ""
    nameHundred = ""

    if part >= 1000000:
        divide = part // 1000000
        part = part % 1000000
        divide1 = divide // 100
        part1 = divide % 100
        nameMillion = digitName(divide1) + " hundred" + processDigit(part1) + " million "

    if part >= 1000:
        divide = part // 1000
        part = part % 1000
        divide1 = divide // 100
        part1 = divide % 100
        nameThousand = digitName(divide1) + " hundred" + processDigit(part1) + " thousand "

    if part >= 100:
        divide = part // 100
        part = part % 100
        nameHundred = digitName(divide) + " hundred" + ' and' + processDigit(part)

        return nameMillion + nameThousand + nameHundred


# process the three digit number
def processDigit(number):
    part = number
    name = ""

    if part >= 20:
        name = name + " " + tensName(part)
        part = part % 10

    elif part >= 10:
        name = name + " " + teenName(part)
        part = 0

    if part > 0:
        name = name + " " + digitName(part)

    return name

# turns a digit into its English name
def digitName(digit):
    if digit == 1: return "one"
    if digit == 2: return "two"
    if digit == 3: return "three"
    if digit == 4: return "four"
    if digit == 5: return "five"
    if digit == 6: return "six"
    if digit == 7: return "seven"
    if digit == 8: return "eight"
    if digit == 9: return "nine"
    return ""


# turns a number between 10 and 19 into its English name
def teenName(number):
    if number == 10: return "ten"
    if number == 11: return "eleven"
    if number == 12: return "twelve"
    if number == 13: return "thirteen"
    if number == 14: return "forteen"
    if number == 15: return "fifteen"
    if number == 16: return "sixteen"
    if number == 17: return "seventeen"
    if number == 18: return "eighteen"
    if number == 19: return "nineteen"
    return ""


# gives the name of tens part of a number between 20 and 99
def tensName(number):
    if number >= 90: return "ninety"
    if number >= 80: return "eighty"
    if number >= 70: return "seventy"
    if number >= 60: return "sixty"
    if number >= 50: return "fifty"
    if number >= 40: return "forty"
    if number >= 30: return "thirty"
    if number >= 20: return "twenty"
    return ""

# start the program
#main()

main(1000)

contains bugs!

eighthundredAND! for ex

correct ans 21124
