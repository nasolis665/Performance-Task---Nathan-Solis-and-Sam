from random import randint

def roll(num, dice):
  if num == dice:
    num=num.replace('d','')
    num = randint(1,num)
    print("You rolled a: " + num)
  else:
    print("That is not a valid number, pick a valid number")
