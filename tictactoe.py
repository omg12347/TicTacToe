import random

BOARD_SIZE = 9
EMPTY_BOX = ' '
HUMAN_MARK = 'X'
COMPUTER_MARK = 'O'
WINNING_COMBOS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6],             # diagonals
]

def print_board(initial=False):
    """
    Print the current state of the board. If this is the beginning of the game,
    print out numbers 1-9 to show players how to pick a box. Otherwise, update
    each box with X or O from the boxes list.
    """
    if initial:
        print('\n'.join(f'{i+1}' for i in range(BOARD_SIZE)))
    else:
        print(f'''
         {boxes[0]} | {boxes[1]} | {boxes[2]} 
        -----------
         {boxes[3]} | {boxes[4]} | {boxes[5]}
        -----------
         {boxes[6]} | {boxes[7]} | {boxes[8]} 
    ''')

def take_turn(player, turn):
    """
    Prompt the player to select an empty box on the board. If the player is
    the computer, select a random empty box instead. Repeat until a valid
    choice is made.
    """
    while True:
        if player == COMPUTER_MARK:
            box = random.randint(0, BOARD_SIZE - 1)
        else:
            box = input(f'Player {player}, choose a box (1-9): ')
            try:
                box = int(box) - 1  # subtract 1 to sync with boxes[] index numbers
            except ValueError:
                print('Invalid input. Try again.\n')
                continue

        if not (0 <= box < BOARD_SIZE):
            print('Box number out of range. Try again.\n')
            continue

        if boxes[box] == EMPTY_BOX:
            boxes[box] = player
            break
        else:
            print('Box already taken. Try again.\n')

def switch_player(turn):
    """
    Determine the current player based on the turn number. The first player
    is always HUMAN_MARK.
    """
    return HUMAN_MARK if turn % 2 == 1 else COMPUTER_MARK

def check_for_win(player, turn):
    """
    Check if the current player has won the game or if it's a tie. If neither,
    return None to continue the game.
    """
    if turn < 2:
        return None

    for combo in WINNING_COMBOS:
        if all(boxes[i] == player for i in combo):
            return 'win'

    if EMPTY_BOX not in boxes:
        return 'tie'

    return None

def play(player, turn):
    """
    Play a game of Tic Tac Toe between two players, where player can be either
    HUMAN_MARK or COMPUTER_MARK. The game continues until a player wins or it's
    a tie.
    """
    while True:
        take_turn(player, turn)
        print_board()
        result = check_for_win(player, turn)
        if result == 'win':
            print(f'Game over. Player {player} wins!')
            break
        elif result == 'tie':
