from dice import *
dice=["d4","d6","d8","d10","d12","d20","d100"]
dices=' '
for x in dice:
  dices += ' or '+ x
num=input("Would you like to roll a" + dices+'? ')
roll(num, dice)

