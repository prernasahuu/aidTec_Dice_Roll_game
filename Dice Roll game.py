import random
def roll_dice_game():
  print("WELCOME TO THE DICE ROLLING GAME!")

  while True:
    one_dice=random.randint(1,6) 
    two_dice= random.randint(1,6)
    guess = int(input("Enter your guess (2 to 12): "))
    sum= one_dice+two_dice
    print(f"DICE 1: {one_dice}")
    print(f"DICE 2: {two_dice}")
    print(f"SUM OF DICE: {sum}")
    
    if guess == sum :
      print(f"CONGRATULATIONS!!")
      print("Bravo!! You're the WINNER.")
      break
    else:
      print(f"Game Over! WRONG GUESS")
      print("PLAY AGAIN?")
      quit = input("Do you want to play again? (yes/quit):")
      if quit.lower()!="yes":
        break
roll_dice_game()
