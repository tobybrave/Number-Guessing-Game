import random

def easy():
  print("\n||LEVEL 1||")
  n = 6
  while n > 0:
    print(f"\n You've {n} guess power")
    try:
      user = eval(input("Guess a number from 1 - 10 : "))
    except:
      print(" Only numbers are allowed!!! Try again")
   
    else:
      comp = random.randint(1,10)
      print("The computer guessed : ",comp)
    
      if user == comp:
        print(" You got it right\n Level Completed!")
        medium()
      else:
        print(" That was wrong")
        n = n-1
  else:
    print(" GAME OVER!!!")
    main()
    
def medium():
  print("\n||LEVEL 2||")
  n = 4
  while n > 0:
    print(f"\n You've {n} guess power")
    try:
      user = eval(input("Guess a number from 1 - 20 : "))
    except:
      print(" Only numbers are allowed!! Try again")
   
    else:
      comp = random.randint(1,20)
      print("The computer guessed : ",comp)
    
      if user == comp:
        print("You got it right\n Level Completed!")
        hard()
      else:
        print("That was wrong")
        n = n - 1
  else:
    print(" GAME OVER!!!")
    main()
    
def hard():
  print("\n||LEVEL 3||")
  n = 3
  while n > 0:
    print(f"\n You've {n} guess power")
    try:
      user = eval(input("Guess a number from 1 - 50 : "))
    except:
      print(" Only numbers are allowed!!! Try again")
    else:
      comp = random.randint(1,50)
      print("The computer guessed : ",comp)
    
      if user == comp:
        print("You got it right\n You are GUESS MASTER!")
        play_again = input(" \nWill you like to play again? \nEnter 'yes' or 'no' : ")
        if play_again == "yes" or play_again == "Yes":
          easy()
        elif play_again == "no" or play_again == "No":
          main()
          
      else:
        print("That was wrong")
        n = n - 1
  else:
    print(" GAME OVER!!!")
    main()
    
def main():
  print("\n+++ LEVEL +++")
  print("Press 1 to select Easy\nPress 2 to select Medium \nPress 3 to select Hard")
  level = True
  while level:
    try:
      level = eval(input("\nSelect a level to play : "))
    except:
      print(" Your input was invalid!!! Only pick a number from 1 - 3")
    else:
      if level == 1:
        easy()
        level = False
      elif level == 2:
        medium()
        level = False
      elif level == 3:
        hard()
        level = False

print("***NUMBER GUESS***")
main()