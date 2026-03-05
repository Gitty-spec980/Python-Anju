# import necessary modules
import random

# pick a number between 1-100
number=random.randint(1, 100)

def intro():
    print('WHAT IS UR NAME?!!!')

    global name 
    name = input()
    print(name +', we r going to play ... A GAMEEE! I am thinking of a number between 1-100')
    if(number%2==0):
        x='even'
    else:
        x= 'odd'
    print('\nThis is a(n) {} number'.format(x))

    print('GO AHEADDD. GUESS NOW BEFORE I SEND U TO MARSSSSSSSS ')

def pick():
        guessesTaken = 0

        
        while guessesTaken < 6:


            enter = input('PUT UR GUESS HERE RIGHT NOWWWW :')
        


            try:

               
                guess = int(enter)

                if guess<=100 and guess>=1:
                    gussesTaken = guessesTaken+1
                    if guessesTaken<6:
                        if guess<number:
                            print('THIS NUMBER IS TOO LOWWWWWWWWW')
                        if guess>number:
                            print('THIS NUMBER IS TOO HIGHHHHHHHHH')
                        if guess !=number:

                            print('DELETE IT RIGHT NOW AND GUESS AGAINNNNNNNNNNNN')
                      
                        if guess==number:
                            break

                if guess>100 or guess<1:
                    print('DUMB DUCK!!! THIS IS NOT EVEVN THE RIGHT NUMBER RANGE :((()))')

                    print('NOW ENTER A NUMBER ONE TO  ONE HUNDREAD BEFORE I SLAP U TOO JUPITER')

            except:
                print("I BELIEVE ITS A NUMBER  "+enter+" REDO ITTTT ")
        if guess == number:
            guessesTaken = str(guessesTaken)
            print('FINE>> U DID WELL I GUESS, {} YOU GUESSED MY NUMBER IN {} TRIES'.format(name, guessesTaken))

        if guess != number:
            print('BWAHAHAHAHAHAHAH... I KNEW YOU CANT GUESS MY NUMBER. Loser... IT WAS ' +str(number))
playagain='yes'
while playagain== "yes" or playagain=="y" or playagain=="Yes" or playagain=="YES":
    intro()
    pick()
    print("DO YOU WANT TO PLAY AGAIN U FILTHY ANIMAL?")
    playagain=input()
    
