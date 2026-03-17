'''We will make this board with a dictionary. Keys will be (1.e : top-left,mid-right,etc.)
Its values will be empty space and after every move change te value according to player's choice of move.'''

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ', 
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

    '''We will print the updated board after each move in the game and thus will make a function in which we'll define the printBoard function o that we can easily print the board everytime by calling this function.'''

def printBoard(board):
    print(board['7'] + '|' +board['8'] + '|' +board['9'])
    print('-+-+-')
    print(board['4'] + '|' +board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' +board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count= 0


    for i in range(10):
        printBoard(theBoard)
        print("Its your turn," + turn + " . WHich place do you want to move to?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print('That plae is already filled. \nWhch other place do you want to fill?') 
            continue

        if count >=5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print('\nGAME OVERRRR\n')
                print(' ****' +turn + "wonnn. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print('\nGAME OVERRRR\n')
                print(' ****' +turn + "wonnn. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print('\nGAME OVERRRR\n')
                print(' ****' +turn + "wonnn. ****")
                break
            elif theBoard['1'] == theBoard['7'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print('\nGAME OVERRRR\n')
                print(' ****' +turn + "wonnn. ****")
                break
            elif theBoard['8'] == theBoard['5'] == theBoard['2'] != ' ':
                printBoard(theBoard)
                print('\nGAME OVERRRR\n')
                print(' ****' +turn + "wonnn. ****")
                break
            elif theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print('\nGAME OVERRRR\n')
                print(' ****' +turn + "wonnn. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print('\nGAME OVERRRR\n')
                print(' ****' +turn + "wonnn. ****")
                break
            elif theBoard['9'] == theBoard['5'] == theBoard['1'] != ' ':
                printBoard(theBoard)
                print('\nGAME OVERRRR\n')
                print(' ****' +turn + "wonnn. ****")
                break

        if count == 9:
            print('\n The games over...\n')
            print('It a tie!')

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input('Play again??? (y/n)')
    if restart == 'y' or restart == "Y":
        for key in board_keys:
            theBoard[key]= " "
            
        game()

if __name__ == "__main__":
    game()

        
