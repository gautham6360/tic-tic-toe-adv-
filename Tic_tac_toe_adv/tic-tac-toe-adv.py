def default():
    print("\nWelcome! Let's play TIC TAC TOE!\n")

def rules():
    print("The board will look like this!")
    print("The positions of this 3 x 3 board is same as the right side of your keyboard.\n")
    print(" 7 | 8 | 9 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 1 | 2 | 3 ")
    print("\nYou just have to input the position(1-9).")

def play():
    return input("\nAre you ready to play the game? Enter [Y]es or [N]o.\t").upper().startswith('Y')

def choice(p1_name):
    p1_choice = ' '
    while p1_choice not in ['X', 'O']:
        p1_choice = input(f"\n{p1_name}, Do you want to be X or O?\t").upper()
        if p1_choice in ['X', 'O']:
            break
        print("INVALID INPUT! Please Try Again!")
    p2_choice = 'O' if p1_choice == 'X' else 'X'
    return (p1_choice, p2_choice)

def first_player():
    import random
    return random.choice([0, 1])

def display_board(board, avail):
    print("    " + " {} | {} | {} ".format(board[7], board[8], board[9]) + "            " + " {} | {} | {} ".format(avail[7], avail[8], avail[9]))
    print("    " + "-----------" + "            " + "-----------")
    print("    " + " {} | {} | {} ".format(board[4], board[5], board[6]) + "            " + " {} | {} | {} ".format(avail[4], avail[5], avail[6]))
    print("    " + "-----------" + "            " + "-----------")
    print("    " + " {} | {} | {} ".format(board[1], board[2], board[3]) + "            " + " {} | {} | {} ".format(avail[1], avail[2], avail[3]))

def player_choice(board, name, choice):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input(f'\n{name} ({choice}), Choose your next position: (1-9) \t'))
        if position not in range(1, 10) or not space_check(board, position):
            print(f"INVALID INPUT. Please Try Again!\n")
    return position

def CompAI(board, choice):
    possibilities = [x for x in range(1, 10) if board[x] == ' ']
    for let in ['O', 'X']:
        for i in possibilities:
            board_copy = board[:]
            board_copy[i] = let
            if win_check(board_copy, let):
                return i
    open_corners = [x for x in possibilities if x in [1, 3, 7, 9]]
    if open_corners:
        return select_random(open_corners)
    if 5 in possibilities:
        return 5
    open_edges = [x for x in possibilities if x in [2, 4, 6, 8]]
    if open_edges:
        return select_random(open_edges)

def select_random(lst):
    import random
    return random.choice(lst)

def place_marker(board, avail, choice, position):
    board[position] = choice
    avail[position] = ' '

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return all(board[i] != ' ' for i in range(1, 10))

def win_check(board, choice):
    return (
        (board[1] == choice and board[2] == choice and board[3] == choice) or
        (board[4] == choice and board[5] == choice and board[6] == choice) or
        (board[7] == choice and board[8] == choice and board[9] == choice) or
        (board[1] == choice and board[4] == choice and board[7] == choice) or
        (board[2] == choice and board[5] == choice and board[8] == choice) or
        (board[3] == choice and board[6] == choice and board[9] == choice) or
        (board[1] == choice and board[5] == choice and board[9] == choice) or
        (board[3] == choice and board[5] == choice and board[7] == choice)
    )

def replay():
    return input('\nDo you want to play again? Enter [Y]es or [N]o: ').lower().startswith('y')

print("\n\t\t HELLO \n")
input("Press ENTER to start!")

default()
rules()

while True:
    theBoard = [' '] * 10
    available = [str(num) for num in range(10)]
    
    print("\n[0]. Player vs. Computer")
    mode = int(input("\nSelect an option [0]: "))
    
    if mode == 0:
        p1_name = input("\nEnter NAME of PLAYER who will go against the Computer:\t").capitalize()
        p2_name = "Computer"
        p1_choice, p2_choice = choice(p1_name)
        print(f"\n{p1_name}: {p1_choice}")
        print(f"{p2_name}: {p2_choice}")

    if first_player():
        turn = p2_name
    else:
        turn = p1_name

    print(f"\n{turn} will go first!")

    play_game = play()

    while play_game:
        if turn == p1_name:
            display_board(theBoard, available)
            position = player_choice(theBoard, p1_name, p1_choice)
            place_marker(theBoard, available, p1_choice, position)
            if win_check(theBoard, p1_choice):
                display_board(theBoard, available)
                print(f"\n\nCONGRATULATIONS {p1_name}! YOU HAVE WON THE GAME!\n")
                play_game = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard, available)
                    print("\nThe game is a DRAW!\n")
                    break
                else:
                    turn = p2_name
        elif turn == p2_name:
            display_board(theBoard, available)
            position = CompAI(theBoard, p2_choice)
            place_marker(theBoard, available, p2_choice, position)
            print(f'\n{p2_name} ({p2_choice}) has placed on {position}\n')
            if win_check(theBoard, p2_choice):
                display_board(theBoard, available)
                print(f"\n\nTHE Computer HAS WON THE GAME!\n")
                play_game = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard, available)
                    print("\nThe game is a DRAW!\n")
                    break
                else:
                    turn = p1_name

    if not replay():
        break

print("\n\n\t\t\t\t\t\t***************************************")
print("\t\t\t\t\t\t************ OK! BYE BYE! ************")
print("\t\t\t\t\t\t***************************************\n\n")

input("Press ENTER to EXIT!")
