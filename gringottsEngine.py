# G R I N G O T T S  E N G I N E

import random
import time

import potions
import magicitems
import character

class Gringotts(object):
  def __init__(self):
    self.flag = False

  def get_money(self, harry_potter):
    print("\n- - - Welcome to Gringotts, the wizard bank. - - -")
    print("You have {} galleons in your pocket.".format(harry_potter.galleons))

    if self.flag == False:
      print("What do you want to do?")
      print("1. Withdraw 1 galleon.")
      print("2. Play a game to earn more galleons.")

      while harry_potter.alive():
        flag = True
        keyinput = int(input("> "))

        if keyinput == 1:
          # ADD ONE GALLEON TO HARRY'S POCKET AND EXIT GRINGOTTS
          harry_potter.galleons += 1
          harry_potter.print_galleons()
          break

        elif keyinput == 2:
          # PLAY A GUESS A NUMBER GAME
          gringotts_riddle = Riddle()
          riddle_outcome = gringotts_riddle.guess_a_number()
          
          if riddle_outcome == True and Riddle.tries == 1:
            # ADD TEN GALLEONS IF WIN ON FIRST TRY
            print("It took you one try. You win 10 galleons!")
            harry_potter.galleons += 10

          elif riddle_outcome == True and Riddle.tries == 2:
            # ADD TWO GALLEONS IF WIN ON SECOND TRY
            print("It took you two tries. You win 2 galleons.")
            harry_potter.galleons += 2

          else:
            # EXIT AFTER TWO FAILED ATTEMPTS
            print("You lost. Try again later.")
          break

        else:
          # EXCEPTION HANDLING
          print("Invalid input {}".format(input))
          continue

    else:
      # IF GRINGOTTS FLAG IS TRUE, EXIT GRINGOTTS
      print("You already visited Gringotts today. Try again later.")

    # PRINT STATEMENT FOR ANY VISIT
    ###################### need to add time thing
    print("Gringotts goblins aren't the nicest of creatures. Better scurry!")

class Riddle(object):
  def __init__(self):
    pass
    
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