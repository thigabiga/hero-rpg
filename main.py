# H A R R Y  P O T T E R  R P G  G A M E

import random
import time

import potions
import magicitems
import character
import engine
import gringottsEngine

# RUN GAME
def run():

  # HERO
  harry_potter = character.Potter()

  # ENEMIES
  # enemies = [draco_malfoy = Draco(), troll = Troll(), 
  # quirrell = Quirrell(), fluffy = Fluffy(), flying_keys = Keys(), 
  # wizard_Chess = (chess), voldy = Voldemort(), neville = Neville()]

  # NAV MAP
  gringotts = gringottsEngine.Gringotts()
  ollivanders = engine.Ollivanders()
  requirement = engine.Requirement()
    
  # CLASS MAP
  charms_class = potions.Charms()
  #potions_class = potions.Potions()

  # WIN FLAG
  win_flag = False

  # MAIN NAVIGATION
  print("\n========================================")
  print("Harry Potter and the Philosopher's Stone")
  print("========================================")

  while harry_potter.alive() and win_flag == False:
    print("\n- - - You're a wizard, Harry! - - -")
    print("1. Enter Diagon Alley")
    print("2. Wait, I'm not Harry!")
    keyinput = int(input("> "))

    if keyinput == 1:

      # DIAGON ALLEY NAVIGATION
      while harry_potter.alive():
        print("\n- - - Welcome to Diagon Alley - - -")
        print("What do you want to do?")
        print("1. Enter Gringotts")
        print("2. Enter Ollivanders")
        print("3. Enter Knockturn Alley")
        print("4. Take the Hogwarts Express")
        keyinput = int(input("> "))   

        # GRINGOTTS WIZARD BANK
        if keyinput == 1:
          gringotts.get_money(harry_potter)

        # OLLIVANDERS WAND SHOP
        elif keyinput == 2:
          ollivanders.get_wand(harry_potter)

        # BORGIN & BURKES KILL BUTTON
        elif keyinput == 3:
          print("You disappeared into the vanishing cabinet at Borgin & Burkes.")
          exit(0)

        elif keyinput == 4:

          # LOOP BACK FOR NO WAND
          if not harry_potter.wand:
            print("You can't go to Hogwarts without a wand.")
            continue

          else:

            # RESET BANK FLAG
            gringotts.flag = False

            # HOGWARTS NAVIGATION
            while harry_potter.alive():
              print("\n- - - Welcome to Hogwarts - - -")
              print("\nWhat do you want to do?")
              print("1. Go to the Great Hall")
              print("2. Go to class")
              print("3. Explore the corridors")
              print("4. Go back to Diagon Alley")
              keyinput = int(input("> "))    

              if keyinput == 1:

                # SORTING HAT FLAG
                if harry_potter.house == "":
                  print("First years, this way to the Sorting Hat.")
                  print("The Sorting Hat says, \"You belong in Gryffindor, where dwell the brave at heart,")
                  print("Their daring, nerve and chivalry set Gryffindors apart.\"")
                  harry_potter.house = "Gryffindor"
                
                else:
                  print("You've already been sorted into Gryffindor.")
                  print("You have {} house points.".format(harry_potter.house_points))

              # CLASS
              elif keyinput == 2:
                charms_class.practice_charms(harry_potter)

              # COORIDORS
              elif keyinput == 3:
                probability = random.random()

                # ROOM OF REQUIREMENT
                if probability < .2:
                  requirement.find_items(harry_potter)
                
                # FIGHT DRACO
                elif probability < .4:
                  pass

                # FINAL FIGHT SEQUENCE
                elif probability < .6:
                  pass
                
                # FIND THE DORM
                elif probability < .8:
                  pass
                
                # FIGHT TROLL
                else:
                  pass
              
              # BREAK FOR DIAGON ALLEY
              elif keyinput == 4:
                break

              # INVALID
              else:
                print("Invalid input {}".format(input))
                continue

          
            
        
        # INVALID
        else:
          print("Invalid input {}".format(input))
          continue  






    # DUDLEY KILL BUTTON
    elif keyinput == 2:
      print("Fine. Goodbye, Dudley.")
      exit(0)

    # INVALID
    else:
      print("Invalid input {}".format(input))
      continue
  
  # WIN FLAG
  if win_flag == True:
    print("You win!")
    exit(0)

if __name__ == "__main__":
  run()

