    
def player_move(board: list[int], score: dict[str, int]):
    """
        Prompts the player to choose a valid move.
        Remember score is a dictionary from play_game()
        It has two keys 'player' and 'ai' associated values
        are 10 and -10 depending on who goes first.
    """
    
    prompt = "Select an empty cell (1-9): "
    while True:
        try:
            # TODO: Convert input to integer
            move = int(input(prompt))
            # TODO: Validate move is in range and not taken
            if move < 1 or move > 9:
                prompt = "Out of range. Choose between 1-9:" #validate move is in range
                continue
            index = move - 1   #index is 0-8 (for move btw 1-9) so have to minus 1
            if abs(board[index]) == 10:
                prompt = "Cell already taken. Choose again: "
                continue
            pass
        except ValueError:
            prompt = "Invalid input. Try again (1-9):"
            
    # TODO: Assign score['player'] to the selected cell on the board
        board[index] = score['player']
        break
    # HINT: remember the board moves are 1 - 9 but the board indices are
    # 0 - 8
pass
