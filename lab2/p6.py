# Define the Tic-Tac-Toe board and players
PLAYER = 'X'
OPPONENT = 'O'
EMPTY = ' '

def is_open_line(line, player):
    """Check if the line (row, column, or diagonal) is open for the given player."""
    if line.count(EMPTY) == 0:  # No empty space left
        return False
    if line.count(player) == 0:  # The player is not present in the line
        return False
    return True

def heuristic(board):
    """Calculate the heuristic value for the given Tic-Tac-Toe board."""
    # Initialize counts
    player_open_lines = 0
    opponent_open_lines = 0
    
    # Check rows and columns
    for i in range(3):
        # Check rows
        row = board[i]
        if is_open_line(row, PLAYER):
            player_open_lines += 1
        if is_open_line(row, OPPONENT):
            opponent_open_lines += 1
        
        # Check columns
        column = [board[j][i] for j in range(3)]
        if is_open_line(column, PLAYER):
            player_open_lines += 1
        if is_open_line(column, OPPONENT):
            opponent_open_lines += 1
    
    # Check diagonals
    diagonal1 = [board[i][i] for i in range(3)]
    diagonal2 = [board[i][2-i] for i in range(3)]
    
    if is_open_line(diagonal1, PLAYER):
        player_open_lines += 1
    if is_open_line(diagonal1, OPPONENT):
        opponent_open_lines += 1
    
    if is_open_line(diagonal2, PLAYER):
        player_open_lines += 1
    if is_open_line(diagonal2, OPPONENT):
        opponent_open_lines += 1
    
    # Heuristic is the difference between open lines for player and opponent
    return player_open_lines - opponent_open_lines

# Example usage
board = [
    ['X', 'O', 'O'],
    ['X', ' ', ' '],
    [' ', 'O', 'X']
]

print("Heuristic Value:", heuristic(board))
