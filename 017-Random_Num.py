import random

# print(help(random))

#  for a random whole integer between the range 1 to 6, i.e. a dice:

# num = random.randint(1, 6)     # here the range is inclusive on both sides. i.e. that the output can be 1 as well as 6.
# print(num)

# ####################################################################################################33
# low=1
# high=100

# num2 = random.randint(low, high)
# print(num2)

##########################################################################################################
# # for the random float , use

# num3 = random.random()     # will print a float between 0 and 1

# print(num3)
##################################################################################################################

# # to choose a random item from a tuple, list ,etc

# options = ("rock", "paper", "scissors")
# option = random.choice(options)
# print(option)

######################################################################
# To Shuffle
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] 
random.shuffle(cards)
print(cards)