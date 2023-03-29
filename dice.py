from random import randint

def roll(num, dice):
  if num in dice:
    num=num.replace('d','')
    num = randint(1,int(num))
    print("You rolled a: " + str(num))
  else:
    print("That is not a valid number, pick a valid number")
