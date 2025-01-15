"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Martin Snajdr
email: martin.snajdr.japan@gmail.com
"""

import random
import time

# Constants
PLAYER_MARKER = "X" #"\U0001F603" 
COMPUTER_MARKER = "O" #"\U0001F916" 
EMPTY = " "
BOARD_SIZE = 3  # Adjustable for larger boards
WINNING_SCORE = 2  # Number of wins needed to win the series

def initialize_board(size: int) -> list[str]:
    """Initializes a NxN game board as a list of empty strings."""
    return [EMPTY] * (size * size)

def print_rules(score: dict[str, int], size: int) -> None:
    """Prints the game rules and the current score."""
    print(f"""
Welcome to Tic Tac Toe - Best of {WINNING_SCORE * 2 - 1}
============================================
Board Size: {size}x{size}
Current Score:
Player: {score['player']} | Computer: {score['computer']}
============================================
GAME RULES:
Each player places one mark per turn on the grid.
The WINNER is the first to place {size} marks in:
* a horizontal,
* vertical, or
* diagonal row.

First to {WINNING_SCORE} wins takes the series!
============================================
Let's start the game \U0001F44D
============================================
""")

def print_board(board: list[str], size: int) -> None:
    """Prints the current game board in a user-friendly format."""
    print("+---" * size + "+")
    for i in range(0, len(board), size):
        row = board[i:i+size]
        print("| " + " | ".join(row) + " |")
        print("+---" * size + "+")

def generate_winning_combinations(size: int) -> list[list[int]]:
    """Generates all possible winning combinations for a NxN board."""
    rows = [[i * size + j for j in range(size)] for i in range(size)]
    cols = [[j * size + i for j in range(size)] for i in range(size)]
    diag1 = [i * size + i for i in range(size)]
    diag2 = [i * size + (size - i - 1) for i in range(size)]
    return rows + cols + [diag1, diag2]

def check_winner(board: list[str], marker: str, size: int) -> bool:
    """Checks if the given marker has won the game."""
    winning_combinations = generate_winning_combinations(size)
    return any(all(board[pos] == marker for pos in combo) for combo in winning_combinations)

def is_draw(board: list[str]) -> bool:
    """Checks if the board is full, resulting in a draw."""
    return EMPTY not in board

def player_move(board: list[str], size: int) -> int:
    """Gets and validates the player's move."""
    while True:
        try:
            move = int(input(f"Player {PLAYER_MARKER} \U0001F603 | Enter your move (1-{size*size}): ")) - 1
            if 0 <= move < size * size and board[move] == EMPTY:
                return move
            print("Invalid move. Try again.")
        except ValueError:
            print(f"Please enter a valid number between 1 and {size*size}.")

def computer_move(board: list[str], size: int) -> int:
    """Determines the computer's move using basic strategy."""
    for move in range(size * size):
        if board[move] == EMPTY:
            board[move] = COMPUTER_MARKER
            if check_winner(board, COMPUTER_MARKER, size):
                board[move] = EMPTY
                return move
            board[move] = EMPTY

    for move in range(size * size):
        if board[move] == EMPTY:
            board[move] = PLAYER_MARKER
            if check_winner(board, PLAYER_MARKER, size):
                board[move] = EMPTY
                return move
            board[move] = EMPTY

    available_moves = [i for i, spot in enumerate(board) if spot == EMPTY]
    return random.choice(available_moves)

def play_game(size: int) -> None:
    """Main function to play the game."""
    score = {"player": 0, "computer": 0}
    round_number = 1

    while True:
        board = initialize_board(size)
        print_rules(score, size)
        print_board(board, size)

        current_turn = "player" if round_number % 2 == 0 else "computer"

        while True:
            if current_turn == "player":
                player_pos = player_move(board, size)
                board[player_pos] = PLAYER_MARKER
                print_board(board, size)

                if check_winner(board, PLAYER_MARKER, size):
                    print("============================================")
                    print("Congratulations, the player WON this round! \U0001F44F	")
                    print("============================================")
                    score["player"] += 1
                    break

                if is_draw(board):
                    print("============================================")
                    print("It's a draw \U0001F91D !")
                    print("============================================")
                    break

                current_turn = "computer"

            else:
                print("============================================")
                print("Computer's turn... \U0001F916")
                time.sleep(1)
                computer_pos = computer_move(board, size)
                board[computer_pos] = COMPUTER_MARKER
                print_board(board, size)

                if check_winner(board, COMPUTER_MARKER, size):
                    print("============================================")
                    print("The computer WON this round! \U0001F622")
                    print("============================================")
                    score["computer"] += 1
                    break

                if is_draw(board):
                    print("============================================")
                    print("It's a draw \U0001F91D !")
                    print("============================================")
                    break

                current_turn = "player"

        if score["player"] == WINNING_SCORE:
            print("============================================")
            print("Player WINS the series! Congratulations! \U0001F3C6")
            print(f"Final Score: Player: {score['player']} | Computer: {score['computer']}")
            print("Thanks for playing! Goodbye!")
            break

        if score["computer"] == WINNING_SCORE:
            print("============================================")
            print("Computer WINS the series! Better luck next time! \U0001F480")
            print(f"Final Score: Player: {score['player']} | Computer: {score['computer']}")
            print("Thanks for playing! Goodbye!")
            break

        while True:
            replay = input("Do you want to play another round? (Y/N): ").strip().upper()
            if replay in {"Y", "N"}:
                break
            print("Invalid input. Please enter Y or N.")
        if replay == "N":
            print(f"Final Score: Player: {score['player']} | Computer: {score['computer']}")
            print("Thanks for playing! Goodbye! \U0001F44B")
            break

        round_number += 1

if __name__ == "__main__":
    play_game(size=BOARD_SIZE)
