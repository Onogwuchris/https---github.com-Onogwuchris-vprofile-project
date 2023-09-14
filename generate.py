#from random import choice
#coin = choice(["Heads", "Tails"])
#print (coin)

#import random
#number = random.randint(1, 10)
#print(number)

#import random

#cards = ["jack", "queen", "king"]
#random.shuffle(cards)
#for card in cards:
 #  print(card)
 
import sys

if len(sys.argv) < 2:
    print("Few arguement")
elif len(sys.argv) > 2:
    print("Too many arguement")
else:
    print("Hello, my name is ", sys.argv[1])
     