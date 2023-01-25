from random import randint
def roll(num):
  if num == (4 or 6 or 8 or 10 or 12 or 20 or 100):
    num = randint(1,num)
    print("You rolled a: " + num)
  else:
    print("That is not a valid number, pick a valid number")
