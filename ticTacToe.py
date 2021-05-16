theBoard = {'A1': ' ', 'A2': ' ', 'A3': ' ',
            'B1': ' ', 'B2': ' ', 'B3': ' ',
            'C1': ' ', 'C2': ' ', 'C3': ' '}
def printBoard(board):
    print(board['A1'] + '|' + board['A2'] + '|' + board['A3'] + ' A')
    print('-+-+-')
    print(board['B1'] + '|' + board['B2'] + '|' + board['B3'] + ' B')
    print('-+-+-')
    print(board['C1'] + '|' + board['C2'] + '|' + board['C3'] + ' C')
    print('1 2 3 ')
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
