import random
print('Hello! Welocme to Rock, Paper, Scissors\n')
player_wins = 0
computer_wins = 0
while True:
    player = input('Enter a choice (Rock, Paper, Scissors):').lower()
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    print(f"\nYou chose {player}, and the computer chose {computer}!")
    if player == computer:
        print(f'Both players selected {player}. It is a tie!')
    elif player == "rock":
        if computer == "scissors":
            print('Rock smashes scissors. You Win!')
            player_wins+=1
        else:
            print('Paper coves rock. WOMP WOMP>> U lost:(')
            computer_wins+=1
    elif player == "paper":
        if computer == "rock":
            print('Paper covers rock u win:)!')
            player_wins+=1
        else:
            print('Scissors Cuts Paper... You lose:(')
            computer_wins+=1
    elif player == "scissors":
        if computer == "paper":
            print('Scissors cuts paper... U WIN:)!')
            player_wins+=1
        else:
            print('Rock smashes scissors... U LOOSE:(')
            computer_wins+=1
    print("You have "+str(player_wins)+" win(s)")
    print('The computer has ' +str(computer_wins)+' win(s)')






    repeat = input('\n PLAY AGAIN?????? (Yes/No):')
    if repeat.lower()!='yes':
        print("THY FOR PLAYING!!!!")
        break