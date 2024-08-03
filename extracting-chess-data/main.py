import os
import matplotlib.pyplot as plt

NUMBER_OF_GAMES = 1
def get_files():
    global NUMBER_OF_GAMES
    filtered_files = []
    files = os.listdir("data")
    while NUMBER_OF_GAMES > 0:
        for file in files:
            if file.endswith(".pgn"):
                filtered_files.append(file)
                NUMBER_OF_GAMES -= 1
    return filtered_files


PLAYER_NAME = "MasseyJack"
isWhite = True
MODE = "normal"
FILES = []
GAME_DATA = []
MOVES = []
POSSIBLE_BEGINNINGS = [f"{i}." for i in range(1, 200)]
POSSIBLE_MOVES = {
    "Castle": "O-O",
    "QueenSideCastle": "O-O-O",
    "Knight": "N",
    "Bishop": "B",
    "Rook": "R",
    "Queen": "Q",
    "King": "K",
    "Capture": "x",
    "Check": "+",
    "Checkmate": "#",
    "Promotion": "=",
}

def load_game_data():
    global PLAYER_NAME, FILES, GAME_DATA, isWhite
    for files in FILES:
        with open(f"data/{files}", "r") as file:
            GAME_DATA.append(f"data/{files}")
            for line in file:
                if line == f"[White {PLAYER_NAME}]\n":
                    isWhite = True
                elif line == f"[Black {PLAYER_NAME}]\n":
                    isWhite = False
                if line.startswith("["):
                    continue
                GAME_DATA.append(line.strip())
        break  # to only parse the first file

def game_data_parser():
    global GAME_DATA, MOVES
    print(f"Beginning parsing of data for {GAME_DATA[0]}")
    for i in range(2, len(GAME_DATA)):
        data = GAME_DATA[i].split(" ")
        #  print(f"{i} : {data}")
        for move in data:
            MOVES.append(move)

def moves_parser():
    global MOVES
    print(f"Beginning parsing of moves in MOVES for {GAME_DATA[0]}")
    for move in MOVES:
        if move in POSSIBLE_BEGINNINGS:
            MOVES.remove(move)
    #  for filter_move in MOVES:
    #    print(filter_move)

def data_extractor(mode="normal"):
    global MOVES, POSSIBLE_MOVES
    knight_moves = []
    bishop_moves = []
    rook_moves = []
    queen_moves = []
    king_moves = []
    if isWhite:
        for i in range(0, len(MOVES), 2):
            if POSSIBLE_MOVES["Knight"] in MOVES[i]:
                knight_moves.append(MOVES[i])
            elif POSSIBLE_MOVES["Bishop"] in MOVES[i]:
                bishop_moves.append(MOVES[i])
            elif POSSIBLE_MOVES["Rook"] in MOVES[i]:
                rook_moves.append(MOVES[i])
            elif POSSIBLE_MOVES["Queen"] in MOVES[i]:
                queen_moves.append(MOVES[i])
            elif POSSIBLE_MOVES["King"] in MOVES[i]:
                king_moves.append(MOVES[i])
    else:
        for i in range(1, len(MOVES), 2):
            if POSSIBLE_MOVES["Knight"] in MOVES[i]:
                knight_moves.append(MOVES[i])
            elif POSSIBLE_MOVES["Bishop"] in MOVES[i]:
                bishop_moves.append(MOVES[i])
            elif POSSIBLE_MOVES["Rook"] in MOVES[i]:
                rook_moves.append(MOVES[i])
            elif POSSIBLE_MOVES["Queen"] in MOVES[i]:
                queen_moves.append(MOVES[i])
            elif POSSIBLE_MOVES["King"] in MOVES[i]:
                king_moves.append(MOVES[i])
    if mode == "debug":
        print(f"Knight moves: {knight_moves}")
        print(f"Bishop moves: {bishop_moves}")
        print(f"Rook moves: {rook_moves}")
        print(f"Queen moves: {queen_moves}")
        print(f"King moves: {king_moves}")
    return knight_moves, bishop_moves, rook_moves, queen_moves, king_moves

def plot_stats():
    knight_moves, bishop_moves, rook_moves, queen_moves, king_moves = data_extractor()
    # number_of_moves = len(MOVES)
    number_of_knight_moves = len(knight_moves)
    number_of_bishop_moves = len(bishop_moves)
    number_of_rook_moves = len(rook_moves)
    number_of_queen_moves = len(queen_moves)
    number_of_king_moves = len(king_moves)
    # create a pie chart
    labels = ["Knight", "Bishop", "Rook", "Queen", "King"]
    sizes = [
        number_of_knight_moves,
        number_of_bishop_moves,
        number_of_rook_moves,
        number_of_queen_moves,
        number_of_king_moves,
    ]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax1.axis("equal")
    plt.show()


def main():
    global FILES, MODE
    FILES = get_files()
    load_game_data()
    game_data_parser()
    moves_parser()
    data_extractor(mode=MODE)
    plot_stats()


if __name__ == "__main__":
    main()
