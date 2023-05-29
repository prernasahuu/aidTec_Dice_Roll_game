import random

def roll_dice(num_dice):
    dice_rolls = []
    for _ in range(num_dice):
        dice_roll = random.randint(1, 6)
        dice_rolls.append(dice_roll)
    return dice_rolls

def dice_game():
    print("Welcome to the Dice Game!")
    print("Roll the dice and see the outcomes.")

    while True:
        num_dice = int(input("Enter the number of dice to roll: "))
        dice_rolls = roll_dice(num_dice)
        
        print("Dice Rolls:", dice_rolls)
        
        play_again = input("Do you want to play again? (yes/quit): ")
        if play_again.lower() != "yes":
            break
dice_game()
