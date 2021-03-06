# H A R R Y  P O T T E R  R P G  G A M E

import random
import time

import potions
import magicitems
import character

# ENGINE CLASSES

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

class Requirement(object):
  flag = False
  items = [magicitems.Cloak(), magicitems.Hogwarts_History(), magicitems.Broom(), magicitems.Remembrall(), magicitems.Flute()]
  def find_items(self, harry_potter):
    print("\n- - - Welcome to the Room of Requirement - - -")
    print("- - - If you have to ask, you will never know. If you know, you need only ask - - -")
    if flag == False:
      while harry_potter.alive():
        flag = True
        print("What do you want to do?")
        print("1. Look for items")
        print("2. Go back to the hallway")
        print("3. Enter the vanishing cabinet")    
        keyinput = int(input("> "))    
        if keyinput == 1:
          keyindex = random.randint(0, 10)
          if keyindex < len(Requirement.items):
            found_object = Requirement.items[keyindex]
            print("You've found a(n) {}.".format(found_object.name))
            found_object.apply(harry_potter)
          else:
            print("Didn't find anything today. Try again later.")
          break
        elif keyinput == 2:
          print("Just remember, if you have to ask, you will never know. If you know, you need only ask.")
        elif keyinput == 3:
          print("You disappeared into the vanishing cabinet.")
          exit(0)
        else:
          print("Invalid input {}".format(input))
          continue
    else:
      print("You already visited the Room of Requirement today. Try again later.")





class DarkArts(object):
  pass











class Play_Chess(object):
  def __init__(self):
    self.name = "wizard chess"
  def apply(self, harry_potter):
    if self not in harry_potter.items:
      harry_potter.items.append(self)
    else:
      harry_potter.knowledge += 2 # need to add chess outcomes for varying knowledge points

