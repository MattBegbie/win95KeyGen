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

#gen standard

def first_three():
    initial_batch = ''
    l = 11 #starts out of range 
    for i in range(3):
        t = random.randint(0,9)
        #rather than having a big if statement showing all of the incompatible 333, 444, 555, etc. i just dont allow triples by checking against last one
        while l == t:
            t = random.randint(0,9)
        l = t
        initial_batch = initial_batch + str(t)
    return initial_batch + '-'
        

def gen_the_rest():
    while True:
        sum = 0
        konked = ''
        for i in range(7) :
            t = random.randint(0,9)
            sum = sum + t
            konked = konked + str(t)
        if sum % 7 == 0:
            return konked
        else: 
            sum = 0
            konked = ''



#run.. or should i say Main()hahahahahahahahahahahh

first = first_three()
rest = gen_the_rest()
full = first + rest
print(full)

