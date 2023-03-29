import sys
import os
import random
import pickle
class Player:
    def __init__(self, name):
        self.name=name
        self.maxhealth=100
        self.health=self.maxhealth
        self.attack=10
        self.gold=10
        self.pots=0
        self.inventory=[]
        self.hand=(" ")
        self.body=(" ")
class Goblin:
  def __init__(self, name):
    self.name=name
    self.maxhealth=17
    self.health=self.maxhealth
    self.attack=6
    self.gold=15
GoblinIG=Goblin("Goblin")
class Zombie:
  def __init__(self, name):
    self.name=name
    self.maxhealth=28
    self.health=self.maxhealth
    self.attack=4
    self.gold=8
ZombieIG=Zombie("Zombie")
class Skeleton:
  def __init__(self, name):
    self.name=name
    self.maxhealth=21
    self.health=self.maxhealth
    self.attack=7
    self.gold=12
SkeletonIG=Skeleton("Skeleton")
class Bandit:
  def __init__(self, name):
    self.name=name
    self.maxhealth=20
    self.health=self.maxhealth
    self.attack=9
    self.gold=25
BanditIG=Bandit("Bandit")
class Mimic:
  def __init__(self, name):
    self.name=name
    self.maxhealth=65
    self.health=self.maxhealth
    self.attack=14
    self.gold=55
MimicIG=Mimic("Mimic")
class Vampire:
  def __init__(self, name):
    self.name=name
    self.maxhealth=156
    self.health=self.maxhealth
    self.attack=23
    self.gold=230
VampireIG=Vampire("Dracula")
class Kraken:
  def __init__(self, name):
    self.name=name
    self.maxhealth=486
    self.health=self.maxhealth
    self.attack=50
    self.gold=500
KrakenIG=Kraken("Kraken")
class Beholder:
  def __init__(self, name):
    self.name=name
    self.maxhealth=202
    self.health=self.maxhealth
    self.attack=25
    self.gold=300
BeholderIG=Beholder("Beholder")
class Tarrasque:
  def __init__(self, name):
    self.name=name
    self.maxhealth=1000
    self.health=self.maxhealth
    self.attack=100
    self.gold=5000
TarrasqueIG=Tarrasque("Big Lizard King")
def main():
    os.system('clear')
    print("Welcome to our game!")
    print("1.) Start")
    print("2.) Load")
    print("3.) Exit")
    option=input("->")
    if option == "1":
        start()
    elif option == "2":
        if os.path.exists("savefile") == True:
            os.system('clear')
            with open('savefile', 'rb') as f:
                global PlayerIG
                PlayerIG = pickle.load(f)
            print("Loaded Save State...")
            option=input(" ")
            start1()
        else:
            print("You have no save file for this game.")
            optioin=input(" ")
            main()
    elif option == "3":
        sys.exit()
    else: 
        main()
	
def start():
	os.system('clear')
	print("Hello what is your name?")
	option=input("->")
	global PlayerIG
	PlayerIG=Player(option)
	start1()
	
def start1():
    os.system('clear')
    print("Name: %s" % PlayerIG.name)
    print("Attack: %i" % PlayerIG.attack)
    print("Health: %i/%i" % (PlayerIG.health, PlayerIG.maxhealth))
    print("Gold: %d"%PlayerIG.gold)
    print("Potions %d"%PlayerIG.pots)
    print("1.) Fight")
    print("2.) Inventory")
    print("3.) Store")
    print("4.) Boss fight")
    print("5.) Save")
    print("6.) Exit")
    option=input("->")
    if option == "1":
    	prefight()
    elif option == "2":
    	inventory()
    elif option == "3":
    	store()
    elif option == "4":
      prebfight()
    elif option == "5":
      os.system('clear')
      with open('savefile', 'wb') as f:
        pickle.dump(PlayerIG, f)
        print("\nGame has been saved!\n")
      option=input(" ")
      start1()
    elif option == "6":
      sys.exit()
    else:
    	start1()
def prefight():
  global enemy
  enemynum = random.randint(1,4)
  if enemynum==1:
    enemy=GoblinIG
  elif enemynum==2:
    enemy=ZombieIG
  elif enemynum==3:
    enemy=SkeletonIG
  elif enemynum==4:
    enemy=BanditIG
  elif enemynum==5:
    enemy=MimicIG
  fight()
def prebfight():
  global enemy
  bossnum=random.randint(1,5)
  if bossnum==1:
    enemy=VampireIG
  elif bossnum==2:
    enemy=KrakenIG
  elif bossnum==3:
    enemy=BeholderIG
  elif bossnum==4:
    enemy=TarrasqueIG
  fight()
def fight():
  os.system('clear')
  print("%s    vs    %s" % (PlayerIG.name, enemy.name))
  print("%s's Health %d/%d  %s's Health: %i/%i" % (PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth))
  print("Potions %i" % PlayerIG.pots)
  print("1.) Attack")
  print("2.) Drink Potion")
  print("3.) Run")
  option=input(" ")
  if option == "1":
    attack()
  elif option == "2":
    drinkpot()
  elif option == "3":
    run()
  else:
    fight()

def attack():
  os.system('clear')
  Pattack= random.randint(PlayerIG.attack / 2, PlayerIG.attack)
  Eattack= random.randint(enemy.attack / 2, enemy.attack)
  if Pattack == PlayerIG.attack/2:
    print("You Miss!")
  else:
    enemy.health -= Pattack
    print("You dealt %i damage!" % Pattack)
  option=input(" ")
  os.system('clear')
  if Eattack == enemy.attack/2:
    print("The enemy missed!")
  else:
    PlayerIG.health -= Eattack
    print("The enemy dealt %i damage!" % Eattack)
  option=input(" ")
  if PlayerIG.health <= 0:
    die()
  elif enemy.health <= 0:
    edie()
  else:fight()

def drinkpot():
  os.system('clear')
  if PlayerIG.pots==0:
    print("You don't have any potions to drink")
    options=input(" ")
    fight()
  else:
    PlayerIG.health+=8
    start1()

def run():
  os.system('clear')
  pass

def die():
  os.system('clear')
  print("You're Dead!")
  print("play again?")
  print("1.) Try again")
  print("2.) End game")
  option=input(" ")
  if option =="1":
    os.system('clear')
    main()
  if option =="2":
    sys.exit()
def edie():
  os.system('clear')
  print("You killed %s" % enemy.name)
  print("You gain %i gold" % enemy.gold) 
  PlayerIG.gold+=enemy.gold
  option=input(" ")
  start1()
  
def store():
  os.system('clear')
  print("Name: %s" % PlayerIG.name)
  print("Gold: %d"%PlayerIG.gold)
  print("Welcome to the store, would you like to buy potions?")
  print("1.) Buy")
  print("2.) Leave")
  option=input(" ")
  if option == "1":
    os.system('clear')
    print("Name: %s" % PlayerIG.name)
    print("Gold: %d"%PlayerIG.gold)
    print("1.) Buy potion:5 gold")
    print("2.) Buy Steel Sword:25 gold")
    print("3.) Buy Diamond Sword:55 gold")
    print("4.) Buy Steel Armour: 50 gold")
    print("5.) Buy Diamond Armour: 110 gold")
    print("6.) Buy Excalibur: 550 gold")
    print("7.) Back")
    option2=input(" ")
    if option2=="1":
      os.system('clear')
      if PlayerIG.gold < 5:
        print("You don't have enough gold")
        option=input(" ")
        store()
      else:
        print("You bought a potion!")
        PlayerIG.gold-=5
        PlayerIG.pots+=1
        option=input(" ")
        store()
    elif option2=="2":
      os.system('clear')
      if PlayerIG.gold < 25:
        print("You don't have enough gold")
        option=input(" ")
        store()
      else:
        print("You bought a Steel Sword")
        PlayerIG.gold-=25
        PlayerIG.inventory+=["Steel Sword"]
        option=input(" ")
        store()
    elif option2=="3":
      os.system('clear')
      if PlayerIG.gold < 55:
        print("You don't have enough gold")
        option=input(" ")
        store()
      else:
        print("You bought a Diamond Sword")
        PlayerIG.gold-=55
        PlayerIG.inventory+=["Diamond Sword"]
        option=input(" ")
        store()
    elif option2== "4":
      os.system('clear')
      if PlayerIG.gold <50:
        print("You don't have enough gold")
        option=input(" ")
        store()
      else:
        print("You bought Steel Armour")
        PlayerIG.gold-=50
        PlayerIG.inventory+=["Steel Armour"]
        option=input(" ")
        store()
    elif option2== "5":
      os.system('clear')
      if PlayerIG.gold <110:
        print("You don't have enough gold")
        option=input(" ")
        store()
      else:
        print("You bought Diamond Armour")
        PlayerIG.gold-=110
        PlayerIG.inventory+=["Diamond Armour"]
        option=input(" ")
        store()
  elif option2==6:
    os.system('clear')
    if PlayerIG.gold<550:
      print("You don't have enough gold")
      option=input(" ")
      store()
    else:
      print("You bought Excalibur")
      PlayerIG.gold-=550
      PlayerIG.inventory +=["Excalibur"]
      option=input(" ")
      store()
  else:
    start1()

def inventory():
  os.system('clear')
  print(PlayerIG.inventory)
  print("1.) Equip an item")
  print("2.) Leave")
  option=input("->")
  if option == "1":
    os.system('clear')
    print(PlayerIG.name)
    print(PlayerIG.inventory)
    print("Which item would you like to equip?")
    option2=input("").lower()
    if (option2 == "steel sword") and ("Steel Sword" in PlayerIG.inventory):
      os.system('clear')
      PlayerIG.hand=("Steel Sword")
      PlayerIG.attack+=8
      print("You equiped a Steel Sword")
      option=input(" ")
      inventory()
    elif(option2=="diamond sword") and ("Diamon Sword" in PlayerIG.inventory):
      os.system('clear')
      PlayerIG.hand=("Diamond Sword")
      PlayerIG.attack+=15
      print("You equiped a Diamond Sword")
      option=input(" ")
      inventory()
    elif(option2=="steel armour") and ("Steel Armour" in PlayerIG.inventory):
      os.system('clear')
      PlayerIG.body=("Steel Armour")
      PlayerIG.maxhealth+=20
      PlayerIG.health+=20
      print("You equiped Steel Armour")
      option=input(" ")
      inventory()
    elif(option2=="diamond armour") and ("Diamond Armour" in PlayerIG.inventory):
      os.system('clear')
      PlayerIG.body=("Diamond Armour")
      PlayerIG.health+=50
      PlayerIG.maxhealth+=50
      print("You equiped Diamond Armour")
      option=input(" ")
      inventory()
    elif(option2=="exaclibur") and ("Excalibur" in PlayerIG.invertory):
      os.system('clear')
      PlayerIG.body=("Excalibur")
      PlayerIG.health+=110
      PlayerIG.maxhealth+=110
      PlayerIG.attack+=50
      print("You equiped Excalibur")
      option=input(" ")
      inventory()
    else:
      print("You don't own this item")
      option=input(" ")
      inventory()
  else:
    start1()