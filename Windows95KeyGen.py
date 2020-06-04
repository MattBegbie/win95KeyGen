#Windows95KeyGen

#rules
    # must be 10 digits long
    #if you add up last 7 digits they must be divisible by 7
    #    ###-#######

    #cannot start with 333, 444, 555, 666, 777, 888, 999
    #final digit cannot be 0, 8, 9

    #OEM is slightly more difficult
    #First 3 digits can be any number between 001-366 (day of year)
    #next two can be any number less than 03 or greater than 95
    # next 1 must be zero
    #next 6 must have sum which is divisible by 7
    #final 5 can be any combination
    #   #####-OEM-#######-#####

#imports
import random 
#vars which i need
#gen standard

def first_three():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    return str(a) + str(b) + str(c)

def check_f():
    if first == '333-' or first == '444-' or first == '555-' or first == '666-' or first == '777-' or first == '888-' or first == '999-':
        goodThree = False
    else:
        goodThree = True
    return goodThree

def gen_the_rest():
    while True:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        e = random.randint(0, 9)
        f = random.randint(0, 9)
        g = random.randint(0, 9)
        sum = a + b + c + d + e + f + g
        if sum % 7 == 0:
            return str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g)
        else: 
            sum = 0



#run
#gen the first three
while True: #apparently there are no do while loops in python.. bruh
    first = first_three() + '-'
    print(first)
    if check_f() == True:
        break
full = first + gen_the_rest()

rest = gen_the_rest()
print(full)
print(full)

