# H A R R Y  P O T T E R  R P G  G A M E

import random
import time
from magicitems import *
from character import *
from engine import *

# POTIONS AND SPELLS CLASSES

class Charms(object):
  flag = False
  items = []
  def practice_charms(self, harry_potter):
    print("\n- - - Welcome to Charms - - -")
    if flag == False:
      print("What do you want to do?")
      print("1. Practice Charms")
      print("2. Go back to the hallway")        
    for item in items:
      item.test(harry_potter)
        elif keyinput == 2:
          print("Bye.")
        else:
          print("Invalid input {}".format(input))
          continue

class Potions(object):
  flag = False
  items = [Wingardium_Leviosa(), Expelliarmus(), Alohamora(), Petrificus_Totalus()]
  def mix_potions(self, harry_potter):
    print("\n- - - Welcome to Potions - - -")
    print("- - - Here you will learn how to brew glory and bottle fame - - -")
    if flag == False:
      while harry_potter.alive():
        flag = True
        print("What do you want to do?")
        print("1. Practice Potions")
        print("2. Go back to the hallway")
        keyinput = int(input("> "))    
        if keyinput == 1:
          for item in items:
              item.test(harry_potter)
        elif keyinput == 2:
          print("Bye.")
        else:
          print("Invalid input {}".format(input))
          continue

class Spell(object):
  def __init__(self):
    self.name = "<undefined>"
    self.instructions = "<undefined>"

  def test(self, harry_potter):
    flag = False
    tries = 0
    print("You have 5 attempts to guess the correct answer to the following clue:")
    print(item.instructions)
    keyinput = input("> ")
    while tries < 6:
        if keyinput.lower() == item.name.lower():
        flag = True
        item.apply(harry_potter, tries)
        else:
        tries += 1
        print("Try again. > {}".format(input))
    else:
        harry_potter.house_points -= 1
        print("Incorrect answer. Deduct 1 house point from {}.".format(harry_potter.house))

  def apply(self, harry_potter, tries):
    if self not in harry_potter.items:
      points_gained = 5 - tries
      harry_potter.items.append(self)
      harry_potter.knowledge += points_gained
      print("You earn {} knowledge points for learning {}.".format(points_gained, self.name))
    else:
      harry_potter.knowledge += 1
      print("You already answered this question."
      print("You earn 1 knowledge point for practicing {}".format(self.name))


class Wingardium_Leviosa(Spell):
  def __init__(self):
    self.name = "Wingardium Leviosa"
    self.instructions = "Swish and Flick!"

class Expelliarmus(Spell):
  def __init(self):
    self.name = "Expelliarmus"
    self.instructions = "Disarm your opponent using Potter's \"signature spell.\""

class Petrificus_Totalus(Spell):
  def __init(self):
    self.name = "Petrificus Totalus"
    self.instructions = "Mandrakes are the antidote for this spell."

class Alohamora(Spell):
  def __init(self):
    self.name = "Alohamora"
    self.instructions = "You don't need a key to unlock doors with this spell."

class Reparo(Spell):
  def __init(self):
    self.name = "Reparo"
    self.instructions = "Broken glasses? No need to worry if you use this spell."
  
class Illuminate(Spell):
  def __init(self):
    self.name = "Finite Incantatum"
    self.instructions = ""

class Wormwood(Spell):
  def __init(self):
    self.name = ""
    self.instructions = ""