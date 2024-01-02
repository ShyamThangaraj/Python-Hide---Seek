import turtle
import random
from random import randint
import time

#used this link "https://www.tinkercad.com/things/j9zvrIWXnmh"
#used this link "https://www.tinkercad.com/things/hU123itZPQK-wooden-bench"
#used this link "https://www.tinkercad.com/things/eCslAGjyQBT-the-playground-park"
#used this link "https://www.tinkercad.com/things/bYWCuMh4LSn-workbench"
#used this link "https://www.tinkercad.com/things/kPA1Dgscpnu-f1-car"
#used this link "https://www.tinkercad.com/things/aftPiLiyrzV-lawn-mower"
#used this link "https://images.thdstatic.com/productImages/be3175de-b615-4d5c-9422-e1af4b40f63c/svn/ridgid-pipe-wrenches-31010-64_1000.jpg"
#used this link "https://www.tinkercad.com/things/jgeEIkf2IUv-living-room"
#used this link "https://www.tinkercad.com/things/5LsXIP1IfOZ-bedroom"
#used this link "https://www.tinkercad.com/things/h7TWtRwYveu-kitchen"
#used this link "https://www.tinkercad.com/things/1FogPHbfBua-camera-controls"
#used this link "https://www.tinkercad.com/things/4c6GpB3beB3-refrigerator"


def Park(Level):
  screen = turtle.Screen()
  screen.setup(width=480,height=330)
  screen.addshape("Map-Park.png")
  screen.bgpic("Map-Park.png")
  print("Welcome user...")
  time.sleep(1)
  Turtle1 = turtle.Turtle()
  Turtle1.ht()
  screen = turtle.Screen()
  screen.addshape("Squirrel.png")
  Turtle1.shape("Squirrel.png")
  Turtle1.speed(3)
  Turtle1.left(90)
  Turtle1.penup()
  PossibleParkPositions = ["The Basketball court", "The Swings", "The carousel", "The bench", "The seesaw", "The park sign", "The skateboard"]
  Position =random.choice(PossibleParkPositions)
  Turtle1.st()
  print("The squirrel in the middle is going to be the hider!")
  time.sleep(1)
  Turtle1.speed(9)
  for i in range(20):
    Turtle1.goto(randint(-200,200), randint(-200,200))
  print("The squirrel is choosing a spot to hide... Please wait for 3 seconds...")
  Turtle1.ht()
  screen.bgpic("3.png")
  time.sleep(1)
  screen.bgpic("2.png")
  time.sleep(1)
  screen.bgpic("1.png")
  time.sleep(1)
  screen.bgpic("Map-Park.png")
  print("The squirrel has moved to it's hiding spot...")
  tries = 0
  time.sleep(2)
  if Level == "hard":
    tries = 3
  elif Level == "easy":
    tries = 5
  print("\nHere are the possible places you can guess: 'The Basketball court', 'The Swings', 'The carousel', 'The bench', 'The seesaw', 'The park sign', 'The skateboard'\nYou have "  + str(tries) + " tries to guess where the turtle is hiding...")
  time.sleep(3)
  for i in range(tries):
    Guess = input("Please enter your guess: ")
    if Guess == Position:
      print("Your guess was correct!")
      return
    elif i == 4:
      print("Your guess was incorrect!")
      break
    elif Guess != Position:
      print("Your guess was incorrect! Please try again!")
  time.sleep(1)
  print("Sorry but all your tries are over... Better luck next time...")
  time.sleep(1)
  print("The squirrel was hiding at: " + Position)
  return

def LivingRoom(Level):
  screen = turtle.Screen()
  screen.setup(width=550,height=330)
  screen.addshape("LivingRoom&Kitchen.png")
  screen.bgpic("LivingRoom&Kitchen.png")
  print("Welcome user...")
  time.sleep(1)
  Turtle3 = turtle.Turtle()
  Turtle3.ht()
  screen = turtle.Screen()
  screen.addshape("Book.png")
  Turtle3.shape("Book.png")
  Turtle3.speed(0)
  Turtle3.left(90)
  Turtle3.penup()
  PossibleParkPositions = ["The TV", "The couch", "The Dining table", "The refrigerator", "The tree", "The desk", "The oven"]
  Position =random.choice(PossibleParkPositions)
  Turtle3.st()
  print("The Book in the middle is going to be the hider!")
  time.sleep(1)
  Turtle3.speed(9)
  for i in range(17):
    Turtle3.goto(randint(-200,200), randint(-200,200))
  print("The Book is choosing a spot to hide... Please wait for 3 seconds...")
  Turtle3.ht()
  screen.bgpic("3.png")
  time.sleep(1)
  screen.bgpic("2.png")
  time.sleep(1)
  screen.bgpic("1.png")
  time.sleep(1)
  screen.bgpic("LivingRoom&Kitchen.png")
  print("The Book has moved to it's hiding spot...")
  time.sleep(1)
  tries = 0
  if Level == "hard":
    tries = 3
  elif Level == "easy":
    tries = 5
  print("\nHere are the possible places you can guess: 'The TV', 'The couch', 'The Dining table', 'The refrigerator', 'The tree', 'The desk', 'The oven'\nYou have " + str(tries) + " tries to guess where the turtle is hiding...")
  time.sleep(3)
  for i in range(tries):
    Guess = input("Please enter your guess: ")
    if Guess == Position:
      print("Your guess was correct!")
      return
    elif i == 4:
      print("Your guess was incorrect!")
      break
    elif Guess != Position:
      print("Your guess was incorrect! Please try again!")
  time.sleep(1)
  print("Sorry but all your tries are over... Better luck next time...")
  time.sleep(1)
  print("The Book was hiding at: " + Position)
  return



def Garage(Level):
  screen = turtle.Screen()
  screen.setup(width=500,height=300)
  screen.addshape("GarageMap.png")
  screen.bgpic("GarageMap.png")
  print("Welcome user...")
  time.sleep(1)
  Turtle2 = turtle.Turtle()
  Turtle2.ht()
  screen.addshape("wrench.png")
  Turtle2.shape("wrench.png")
  Turtle2.speed(0)
  Turtle2.left(90)
  Turtle2.penup()
  PossibleParkPositions = ["The pingpong table", "Christmas tree", "The workbench", "The TV", "The Arcade", "The car", "The lawn mower", "The cabinet", "The lamp"]
  Position =random.choice(PossibleParkPositions)
  Turtle2.st()
  print("The wrench in the middle is going to be the hider!")
  Turtle2.speed(9)
  time.sleep(1)
  for i in range(20):
    Turtle2.goto(randint(-200,200), randint(-200,200))
  print("The wrench is choosing a spot to hide... Please wait for 3 seconds...")
  Turtle2.ht()
  screen.bgpic("3.png")
  time.sleep(1)
  screen.bgpic("2.png")
  time.sleep(1)
  screen.bgpic("1.png")
  time.sleep(1)
  screen.bgpic("GarageMap.png")
  print("The wrench has moved to it's hiding spot...")
  time.sleep(2)
  tries = 0
  if Level == "hard":
    tries = 3
  elif Level == "easy":
    tries = 5
  print("\nHere are the possible places you can guess: 'The pingpong table', 'Christmas tree', 'The workbench', 'The TV', 'The Arcade', 'The car', 'The lawn mower', 'The cabinet', 'The lamp'\nYou have " + str(tries) +  " tries to guess where the wrench is hiding...")
  time.sleep(3)
  for i in range(tries):
    Guess = input("Please enter your guess: ")
    if Guess == Position:
      print("Your guess was correct!")
      return
    elif i == 4:
      print("Your guess was incorrect!")
      break
    elif Guess != Position:
      print("Your guess was incorrect! Please try again!")
  time.sleep(1)
  print("Sorry but all your tries are over... Better luck next time...")
  time.sleep(1)
  print("The wrench was hiding at: " + Position)
  return

def MapSelection():
  while True:
    Map = input("Please enter 'Park' or 'Garage' or 'Living Room' to choose a map or 'End' to end: ")
    if Map.lower() != "garage" and Map.lower() != "park" and Map.lower() != "living room" and Map.lower() != "end":
      print("Invalid Input! Please try again!")
    elif Map.lower() == "end":
      print("Thanks for playing with us! & Have a great day!")
      return("end")
    else:
      return Map

def LevelSelection():
  while True:
    Level = input("Please enter 'hard' or 'easy' to select level: ")
    if Level != 'hard' and Level != 'easy':
      print("Invalid input! Please try again!")
    else:
      return Level

def introduction():
  while True:
    Map = MapSelection()
    if Map.lower() == "end":
      return
    Level = LevelSelection()
    if Map.lower() == "garage":
      Garage(Level)
    elif Map.lower() == "park":
      Park(Level)
    else:
      LivingRoom(Level)

introduction()
