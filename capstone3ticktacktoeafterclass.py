import random


dice_result = {'side': ' '}


def printDice(dice):
    print("\n+-------+")
    print("|       |")
    print("|   " + str(dice['side']) + "   |")
    print("|       |")
    print("+-------+")

def game():
    print("--- Welcome to the Dice Simulator ---")
    
    
    rolling = True
    while rolling:
        print("\nRolling the dice...")
        
        
        result = random.randint(1, 6)
        
        
        dice_result['side'] = result
        
       
        printDice(dice_result)
        
        
        choice = input("Roll again? (y/n): ")
        
        if choice.lower() != 'y':
            rolling = False

    
    restart = input('\nPlay the game from the beginning??? (y/n): ')
    if restart == 'y' or restart == "Y":
        dice_result['side'] = ' ' 
        game()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    game()





