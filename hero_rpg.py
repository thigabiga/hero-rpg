# Hero = Harry Potter RPG Game

import random
import time

class Character(object):
  def __init__(self):
    self.name = '<undefined>'
    self.health = 10
    self.power = 5
    self.coins = 20

  def alive(self): # default alive iff health > 0
    return self.health > 0

  def print_status(self):
    if self.alive():
      print("{} has {} health and {} power.".format(self.name, self.health, self.power))
    else:
      print("{} is dead.".format(self.name))

  def attack(self, enemy, items = []): #attack dependent on enemy and list of items
    if self.alive():
      damage = enemy.receive_damage(self, items)
      print("{} does {} damage to {}.".format(self.name, damage, enemy.name))

  def receive_damage(self, enemy, extra_damage = 0):
    if self.alive():
      damage = enemy.power + extra_damage
      self.health -= damage
      return damage

class Potter(Character): #Hero
  def __init__(self):
    self.name = "Harry Potter"
    self.health = 10
    self.power = 5
    self.galleons = 20
    self.armor = 0
    self.evade = 0
    self.wand = False
    self.house = ""
    self.items = []
    self.protection = 5
    self.knowledge = 1

  def attack(self, enemy):
    if self.alive():
      probability = random.randint(1, 5)
      if probability == 1:
        damage = enemy.receive_damage(self, self.power)
      else:
        damage = enemy.receive_damage(self)
      print("{} does {} damage to {}.".format(self.name, damage, enemy.name))
      if not self.alive():
        print("{} is dead.".format(self.name))
      if not enemy.alive():
        self.coins += enemy.coins
        print("{} is dead.".format(enemy.name))

  def receive_damage(self, enemy, extra_damage = 0):
    if self.alive():
      probability = random.randint(1, evade)
      if self.evade > 0 and probability == 1:
        damage = 0
      else:
        damage = enemy.power + extra_damage - self.armor
      self.health -= damage
      return damage

class Death_Eater(Character): #Goblin
  def __init__(self):
    self.name = "Bellatrix Lestrange"
    self.health = 6
    self.power = 2
    self.coins = 5

class Nagini(Character): #Medic
    
  def __init__(self):
    self.name = "Nagini"
    self.health = 6
    self.power = 2
    self.coins = 2

  def receive_damage(self, enemy, extra_damage = 0):
    if self.alive():
      probability = random.randint(1, 5)
      if probability == 1:
        damage = enemy.power + extra_damage - 2
        print("{} gained 2 health.".format(self.name))
      else:
        damage = enemy.power + extra_damage
      self.health -= damage
      return damage

class Dementor(Character): #Shadow
    
  def __init__(self):
    self.name = "Dementor #1"
    self.health = 1
    self.power = 4
    self.coins = 1

  def receive_damage(self, enemy, extra_damage = 0):
    if self.alive():
      probability = random.randint(1, 10)
      if probability == 1:
        damage = enemy.power + extra_damage
      else:
        damage = 0
      self.health -= damage
      return damage

class Voldemort(Character): #Zombie
    
  def __init__(self):
    self.name = "Voldemort"
    self.health = 2
    self.power = 8
    self.coins = 20
    self.horcruxes = 7

  def alive(self):
    return self.health > 0 and self.horcruxes >= 0


class Pettigrew(Character): #Another Character
    
  def __init__(self):
    self.name = "Peter Pettigrew"
    self.health = 1
    self.power = 1
    self.coins = 6

  def receive_damage(self, enemy, extra_damage = 0):
    if self.alive():
      probability = random.randint(1, 2)
      if probability == 1:
        damage = 0
        print("Peter Pettigrew turned into a rat for a minute.")
      else:
        damage = enemy.power + extra_damage
      self.health -= damage
      return damage

class Umbridge(Character): #Another Character
  def __init__(self):
    self.name = "Dolores Umbridge"
    self.health = 4
    self.power = 3
    self.coins =10

  def attack(self, enemy):
    if self.alive():
      probability = random.randint(1, 3)
      if probability == 1:
        damage = enemy.receive_damage(self, 4)
        print("{} says, '{} must not tell lies.'".format(self.name, enemy.name))
      else:
        damage = enemy.receive_damage(self)
      print("{} does {} damage to {}.".format(self.name, damage, enemy.name))
      if not self.alive():
        print("{} is dead.".format(self.name))
      if not enemy.alive():
        print("{} is dead.".format(enemy.name))

  def receive_damage(self, enemy, extra_damage = 0):
    if self.alive():
      probability = random.randint(1, 2)
      if probability == 1:
        damage = 0
      else:
        damage = enemy.power
      self.health -= damage
      return damage

class Tonic(object):
  cost = 5
  name = "tonic"
  def __init__(self, character):
    character.health = 10
    print("{}'s heath increased to 10.".format(character.name))

class Armor(object):
  cost = 6
  name = "armor"
  def __init__(self, character):
    character.armor += 2
    print("{}'s armor increased to {}.".format(character.name, character.armor))  

class Evade(object):
  cost = 2
  name = "Expelliarmus"
  def __init__(self, character):
    character.evade += 2
    print("{}'s Expelliarmus points increased to {}.".format(character.name, character.evade))

class Invisibility(object):
  cost = 10
  name = "Invisibility Cloak"
  def __init__(self, character):
    character.invisibility += 10
    print("{}'s Invisibility Cloak points increased to {}.".format(character.name, character.invisibility))

class Elixer(object):
  cost = 15
  name = "Elixer of Life"
  def __init__(self, character):
    character.elixer += 20
    print("{}'s Elixer of Life points increased to {}.".format(character.name, character.invisibility))

class Dobby(object):
  pass

class Main_Navigation(object):
  def navigate(self, harry_potter):
    print("\n=========================================")
    print("Harry Potter and the Philosopher's Stone")
    print("=========================================")
    while harry_potter.alive():
      harry_potter.print_status()
      time.sleep(1.5)
      print("\n- - - You're a wizard, Harry! - - -")
      print("1. Enter Diagon Alley")
      print("2. Wait, I'm not Harry!")
      keyinput = int(input("> "))
      if keyinput == 1:
        diagon_alley = Diagon_Alley()
        diagon_alley.navigate(harry_potter)
      elif keyinput == 2:
        print("Fine. Goodbye, Dudley.")
        exit(0)
      else:
        print("Invalid input {}".format(input))
        continue

class Diagon_Alley(object):
  def navigate(self, harry_potter):
    while harry_potter.alive():
      time.sleep(1)
      print("\n- - - Welcome to Diagon Alley - - -")
      print("What do you want to do?")
      print("1. Enter Gringotts")
      print("2. Enter Ollivanders")
      print("3. Enter Knockturn Alley")
      print("4. Take the Hogwarts Express")
      keyinput = int(input("> "))    
      if keyinput == 1:
        gringotts = Gringotts()
        gringotts.get_money(harry_potter)
      elif keyinput == 2:
        ollivanders = Ollivanders()
        ollivanders.get_wand(harry_potter)
      elif keyinput == 3:
        print("You disappeared into the vanishing cabinet at Borgin & Burkes.")
        print("Goodbye.")
        exit(0)
      elif keyinput == 4:
        if harry_potter.wand:
          hogwarts = Hogwarts()
          hogwarts.hogwarts_express(harry_potter)
        else:
          print("You haven't purchased your wand yet.")
          continue
      else:
        print("Invalid input {}".format(input))
        continue    

class Gringotts(object):
  def get_money(self, harry_potter):
    time.sleep(1)
    print("\n- - - Welcome to Gringotts, the wizard bank. - - -")
    print("You have {} galleons in your pocket.".format(harry_potter.galleons))
    print("What do you want to do?")
    print("1. Withdraw 5 galleons.")
    print("2. Guess a number to win more galleons.")
    while harry_potter.alive():
      keyinput = int(input("> "))
      if keyinput == 1:
        harry_potter.galleons += 5
        break
      elif keyinput == 2:
        gringotts_riddle = Riddle()
        riddle_outcome = gringotts_riddle.guess_a_number()
        if riddle_outcome == True and Riddle.tries == 1:
          print("It took you one try. You win 10 galleons!")
          harry_potter.galleons += 10
        elif riddle_outcome == True and Riddle.tries == 2:
          print("It took you two tries. You win 1 galleon.")
        else:
          print("You lost. Try again later.")
        break
      else:
        print("Invalid input {}".format(input))
        continue  
    print("You now have {} galleons in your pocket.".format(harry_potter.galleons))
    print("Gringotts goblins aren't the nicest of creatures. Better scurry!")

class Ollivanders(object):
  def get_wand(self, harry_potter):
    print("\n- - - Welcome to Ollivander's, the best wandmaker in London - - -")
    if harry_potter.wand:
      print("You already purchased your wand.")
    else:
      print("The wand chooses the wizard, Harry.")
      print("Yours is 11\" long, made of holly, with a phoenix feather core.")
      print("That'll be 10 galleons.")
      harry_potter.galleons -= 10
      print("You now have {} galleons in your pocket.".format(harry_potter.galleons))
      harry_potter.wand = True
  
class Riddle(object):
  def guess_a_number(self):
    tries = 0
    secret = random.randint(1, 10)
    print("Guess a number between 1 and 10. You have 2 tries.")
    while tries < 2:
      keyinput = int(input("> "))
      if keyinput == secret:
        tries = 2
        return True
      elif keyinput in range(1, 10) and keyinput != secret and tries < 2:
        tries += 1
        if tries < 2:
          print("Try again.")
        continue
      elif keyinput in range(1, 10) and keyinput != secret and tries == 2:
        return False
      else:
        print("Invalid input {}".format(input))
        continue

class Hogwarts(object):
  def hogwarts_express(self, harry_potter):
    print("\n- - - Welcome to Hogwarts - - -")
    if harry_potter.house == "":
      time.sleep(1)
      print("First years, this way to the Sorting Hat:")
      time.sleep(1)
      print("You might belong in Gryffindor, where dwell the brave at heart,")
      time.sleep(1)
      print("Their daring, nerve and chivalry set Gryffindors apart.")
      time.sleep(1)
      print("Yep, better be...Gryffindor!")
      harry_potter.house == "Gryffindor"
    while harry_potter.alive():
      print("\nWhat do you want to do?")
      print("1. Go to Potions class")
      print("2. Go to Defense Against the Dark Arts class")
      print("3. Enter the Room of Requirement")
      print("4. Enter the Forbidden Forest")
      print("5. Take the stairs to Gryffindor dormatory")
      print("6. Go back to Diagon Alley")
      keyinput = int(input("> "))    
      if keyinput == 1:
        potions = Potions(harry_potter)
        potions.make_potions
      elif keyinput == 2:
        dark_arts = Dark_Arts(harry_potter)
        dark_arts.fight_sequence(harry_potter)
      elif keyinput == 3:
        requirement = Requirement()
        requirement.find_items(harry_potter)
      elif keyinput == 4:
        forest = Forest(harry_potter)
        forest.fight_sequence(harry_potter)
      elif keyinput == 5:
        stairs = Stairs(harry_potter)
        stairs.fight_sequence(harry_potter)
      elif keyinput == 6:
        break
      else:
        print("Invalid input {}".format(input))
        continue

class Cloak(object):
  name = "Invisibility Cloak"
  def apply(self, harry_potter):
    harry_potter.items.append(self)
    harry_potter.protection += 5
    print("{}'s protection increased to {}.".format(harry_potter.name, harry_potter.protection))

class Hogwarts_History(object):
  name = "Hogwarts, A History"
  def apply(self, harry_potter):
    harry_potter.items.append(self)
    harry_potter.knowledge += 3
    print("{}'s knowledge increased to {}.".format(harry_potter.name, harry_potter.knowledge))

class Broom(object):
  name = "Nimbus 2000"
  def apply(self, harry_potter):
    harry_potter.items.append(self)
    harry_potter.agility += 3
    print("{}'s agility increased to {}.".format(harry_potter.name, harry_potter.agility))

class Sock(object):
  name = "sock"
  def apply(self, harry_potter):
    harry_potter.items.protection(self)
    harry_potter.protection += 1
    print("{}'s protection increased to {}.".format(harry_potter.name, harry_potter.protection))

class Requirement(object):
  items = [Cloak, Hogwarts_History, Broom, Sock] # need to make objects for all of these items
  def find_items(self, harry_potter):
    print("\n- - - Welcome to the Room of Requirement - - -")
    while harry_potter.alive():
      print("What do you want to do?")
      print("1. Look for items")
      print("2. Go back to the hallway")
      print("3. Enter the vanishing cabinet")    
      keyinput = int(input("> "))    
      if keyinput == 1:
        item_found = Requirement.items[random.randint(0, 3)]
        if item_found not in harry_potter.items:
          print("You've found a(n) {}. Add it to your collection.".format(item_found))
          item_found.apply(harry_potter)
        else:
          print("Didn't find anything today. Try again later.")
        break
      elif keyinput == 2:
        print("If you have to ask, you will never know. If you know, you need only ask.")
        break
      else:
        print("Invalid input {}".format(input))
        continue



def run():
  harry_potter = Potter()
  navigation_engine = Main_Navigation()
  navigation_engine.navigate(harry_potter)
  
  # harry_potter = Potter()
  # enemy = Umbridge()
  
  # while enemy.alive() and harry_potter.alive():
  #   harry_potter.print_status()
  #   enemy.print_status()
  #   print()
  #   print("What do you want to do?")
  #   print("1. Fight {}".format(enemy.name))
  #   print("2. Do nothing")
  #   print("3. Flee")
  #   print("> ", end=' ')
  #   raw_input = input()
  #   if raw_input == "1":
  #     # Potter attacks goblin
  #     harry_potter.attack(enemy)
  #   elif raw_input == "2":
  #     pass
  #   elif raw_input == "3":
  #     print("Goodbye.")
  #     break
  #   else:
  #     print("Invalid input {}".format(raw_input))

  #   enemy.attack(harry_potter)

if __name__ == "__main__":
  run()

