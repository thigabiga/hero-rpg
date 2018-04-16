# H A R R Y  P O T T E R  R P G  G A M E

import random
import time

# CHARACTER CLASSES

class Character(object):
  def __init__(self):
    self.name = "<undefined>"
    self.galleons = 20
    self.wand = False
    self.house = ""
    self.items = []
    self.protection = 1
    self.knowledge = 1
    self.health = 1
    self.house_points = 0

  def alive(self):
    return self.health > 0

  def print_status(self):
    if self.alive():
      print(self.name)
      print("Galleons: {}, Protection: {}, Knowledge: {}, Health: {}".format(self.galleons, self.protection, self.knowledge, self.health))
      print("Items: {}".format(self.items))
      print("{} House Points: {}".format(self.house, self.house_points))
    else:
      print("{} is dead.".format(self.name))

  def attack(self, enemy, weapon):
    if self.alive():
      damage = enemy.receive_damage(self, weapon)
      print("{} does {} damage to {}.".format(self.name, damage, enemy.name))

  def receive_damage(self, enemy, extra_damage = 0):
    if self.alive():
      damage = enemy.strength + extra_damage - self.protection
      self.health -= damage
      return damage

class Potter(Character): #Hero
  def __init__(self):
    self.name = "Harry Potter"
    self.galleons = 20
    self.wand = False
    self.house = ""
    self.items = []
    self.protection = 5
    self.knowledge = 1
    self.health = 2
    self.house_points = 0

  def attack(self, enemy):
    if self.alive():
      probability = random.random()
      if probability > 0.8:
        damage = enemy.receive_damage(self, self.strength)
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
        damage = enemy.strength + extra_damage - self.armor
      self.health -= damage
      return damage
    
  def print_galleons(self):
      print("You have {} galleons in your pocket.".format(self.galleons))


class Draco(Character):
  pass

class Troll(Character):
  pass

class Quirrell(Character):
  pass

class Voldemort(Character):
  pass

class Keys(Character):
  pass

class Chess(Character):
  pass
  
class Fluffy(Character):
    pass