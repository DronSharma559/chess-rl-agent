import chess
import random

def play_random_move():
    # Start a standard chess board
    board = chess.Board()
    print("--- Phase 1: Environment Check ---")
    
    # Get all legal moves
    legal_moves = list(board.legal_moves)
    
    # Choose a move at random (The baseline 'Dumb Agent')
    move = random.choice(legal_moves)
    
    print(f"Board FEN: {board.fen()}")
    print(f"Agent chose move: {move}")
    
    # Apply the move
    board.push(move)
    print("\nBoard after move:")
    print(board)

if __name__ == "__main__":
    play_random_move()
