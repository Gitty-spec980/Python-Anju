import random
print('TAKE MY QUIZ LUVVVVV')
player_wins = 0
computer_wins = 0
while True:
    player = input('What room do Ghosts avoid?').lower()
    choices = ["The kitchen","The playground","The living room"]
    computer = random.choice(choices)
    print(f"\nYou chose {player}, and the computer chose {computer}!")
    if player == computer:
        print(f'Both players selected {player}. It is a tie!')
    elif player == "The living room":
        if computer == "The kitchen":
            print('The living room is the right answer. You Win!')
            player_wins+=1
        else:
            print(' WOMP WOMP>> U lost:(')
            computer_wins+=1
    elif player == "The living room":
        if computer == "The playground":
            print(' u win:)!')
            player_wins+=1
        else:
            print(' You lose:(')
            computer_wins+=1
    print("You have "+str(player_wins)+" win(s)")
    print('The computer has ' +str(computer_wins)+' win(s)')






    repeat = input('\n PLAY AGAIN?????? (Yes/No):')
    if repeat.lower()!='yes':
        print("THY FOR PLAYING!!!!")
        break