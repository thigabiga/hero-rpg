# H A R R Y  P O T T E R  R P G  G A M E

import random
import time
from potions import *
from character import *
from engine import *

# ITEM CLASSES

class Magic_Item(object):
  def __init__(self):
    self.name = "<undefined>"
    self.instructions = "<undefined>"
  
  def apply(self, harry_potter):
    if self not in harry_potter.items:
      harry_potter.items.append(self)
    else:
      print("You already have this item.")

  def use_item(self, harry_potter):
    pass

class Cloak(Magic_Item):
  def __init__(self):  
    self.name = "Invisibility Cloak"
    self.instructions = "Use it well."

class Hogwarts_History(Magic_Item):
  def __init__(self):  
    self.name = "copy of Hogwarts, A History"
    self.instructions = "Honestly, don't you read?"

class Broom(Magic_Item):
  def __init__(self):
    self.name = "Nimbus 2000"
    self.instructions = "It's the fastest broom yet."

class Remembrall(Magic_Item):
  def __init__(self):  
    self.name = "Remembrall"
    self.instructions = ""

class Flute(Magic_Item):
  def __init__(self):
    self.name = "flute"
    self.instructions = ""