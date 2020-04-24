
def make_board():
    return list(" " for n in range (0,9))


def print_board(board):
    print "\n"
    print board[0] +'|'+ board[1] +'|' + board[2]
    print "______"
    print board[3] +'|'+ board[4] +'|' + board[5]
    print "______"
    print board[6] +'|'+ board[7] +'|' + board[8]
    print "\n==========\n"

def space_taken(board,space):
    return ( board[space] != " ")

def game_tied(board):
    return (not ' ' in board)

def game_won(board):
    return (
        ((board[0] == board[1] == board[2]) and (board[0] != ' ')) or
        ((board[3] == board[4] == board[5]) and (board[3] != ' ')) or
        ((board[6] == board[7] == board[8]) and (board[6] != ' ')) or

        ((board[0] == board[3] == board[6]) and (board[0] != ' ')) or
        ((board[1] == board[4] == board[7]) and (board[1] != ' ')) or
        ((board[2] == board[5] == board[8]) and (board[2] != ' ')) or

        ((board[0] == board[4] == board[8]) and (board[4] != ' ')) or
        ((board[2] == board[4] == board[6]) and (board[4] != ' '))
        )

board=make_board()
print_board(board)

markers=["X","O"]

p1_marker = raw_input("Player one, choose X or O: ").upper()
while ("XO".find(p1_marker)==-1 ):
    p1_marker = raw_input("Invalid choice: Choose X or O: ").upper()
p2_marker = markers[(markers.index(p1_marker)+1) % 2]

player_marker_list=[p1_marker,p2_marker]

print 'Player 1 is ' + p1_marker + ', Player 2 is ' + p2_marker
print 'Let\'s begin.\n'
current_player = 1

while not game_won(board) and not game_tied(board):
    print 'Player ' + str(current_player)
    board_position = input("Choose your square: ")
    if ( (board_position-1) not in range (0,9) ):
        board_position = input("Invalid position number: Choose 1-9: ")
    elif ( space_taken(board,board_position-1)  ):
        print 'Space taken, choose another: \n';
    else:
        board[board_position-1]=player_marker_list[current_player-1]
        print '\n'
        print_board(board)
        if game_won(board):
            print 'Player ' + str(current_player) + ' wins!\n'
        elif game_tied(board):
            print 'Tie game.\n'
        else:
            if current_player == 1:
                current_player = 2
            else:
                current_player = 1
