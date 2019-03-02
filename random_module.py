
# importing random module
import random

rolling = True

# create a while loop that rolls until the first digit is 2 or less
# and the second is 10 or less

while rolling:
    x = random.randint(0,99)

    y = random.randint(0,99)

    if x < 2 and 0 < y < 10:
        print( "you rolled a {},{}".format(x,y))
        rolling = False

    else :
        print ("Try again")