from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit
import numpy as np
import os
import time
import json

TOTAL_PLAYERS = 3
BOARD_DIM = (4,4)
ALL = ["cross", "circle", "triangle"]

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET')
socketio = SocketIO(app)

board_size = BOARD_DIM[0] * BOARD_DIM[1]
current_players = []
player_turn = 0
game_in_progress = False
game_board = np.zeros((16,), dtype=np.uint8)
win_check = None # set just before the app starts

@socketio.on('connect')
def new_player(auth):
    global current_players
    if len(current_players) < TOTAL_PLAYERS:
        session["player"] = next(x for x in ALL if x not in current_players)
        current_players.append(session["player"])
        emit("set_user", json.dumps([session["player"]]))
        wait_check(False)
    else:
        session["player"] = "spectator"
        emit("set_user", json.dumps([session["player"]]))
        emit("load_game_board", set_game_board(False))
        emit("load_bottom", set_bottom("game" if game_in_progress else "pregame"))

@socketio.on('disconnect')
def old_player():
    global current_players, game_in_progress
    if session["player"] != "spectator":
        current_players.remove(session["player"])
        if game_in_progress:
            game_in_progress = False
            emit("load_bottom", set_bottom("disconnect"), broadcast=True)

@socketio.on('move')
def register_move(cell_id):
    global game_board, player_turn, game_in_progress
    player_num = ALL.index(session["player"]) + 1
    game_board[int(cell_id)] = player_num
    if check_for_win():
        game_in_progress = False
        emit("load_bottom", set_bottom("win"), broadcast=True)
    elif check_for_draw():
        game_in_progress = False
        emit("load_bottom", set_bottom("draw"), broadcast=True)
    else:
        player_turn = (player_turn + 1) % TOTAL_PLAYERS
        emit("load_bottom", set_bottom("game"), broadcast=True)
    emit("load_game_board", set_game_board(False), broadcast=True)
    
@socketio.on('restart')
def restart_game():
    if not game_in_progress:
        wait_check(True)

@app.route('/')
def index():
    return render_template("index.html")

def new_game():
    global game_in_progress, player_turn, game_board
    game_in_progress = True
    player_turn = time.localtime().tm_sec % TOTAL_PLAYERS
    game_board = np.zeros((16,), dtype=np.uint8)

def wait_check(do_broadcast):
    if len(current_players) == TOTAL_PLAYERS: # wait is over
        new_game() # initialize a new game
        emit("load_game_board", set_game_board(True), broadcast=True) # load new game board
        emit("load_bottom", set_bottom("game"), broadcast=True) # load new bottom
    else:
        emit("load_game_board", set_game_board(False), broadcast=do_broadcast) # load old game board
        emit("load_bottom", set_bottom("pregame"), broadcast=do_broadcast) # load new bottom

def set_game_board(is_new_game):
    cell_owners = ["" if game_board[i] == 0 else ALL[game_board[i]-1] for i in range(board_size)]
    json_game_board = {"gameboard": []}
    json_game_board["gameboard"].append({"new_game": "true" if is_new_game else "false"})
    current_player_turn = ALL[player_turn] if game_in_progress else ""
    json_game_board["gameboard"].append({"player_turn": current_player_turn})
    for i in range(board_size):
        cell_info = {"owner": cell_owners[i]}
        json_game_board["gameboard"].append(cell_info)
    return json.dumps(json_game_board)

def set_bottom(context):
    if context == "pregame":
        args = {
            "turn": "",
            "game_message_display": "flex", 
            "game_message_text": ""
        }
    elif context == "game":
        args = {
            "turn": ALL[player_turn],
            "game_message_display": "none", 
            "game_message_text": ""
        }
    elif context == "disconnect":
        args = {
            "turn": "",
            "game_message_display": "flex", 
            "game_message_text": "A player has disconnected"
        }
    elif context == "win":
        args = {
            "turn": "",
            "game_message_display": "flex", 
            "game_message_text": ALL[player_turn].capitalize() + " wins!"
        }
    elif context == "draw":
        args = {
            "turn": "",
            "game_message_display": "flex", 
            "game_message_text": "Draw!"
        }
    args["type"] = context
    return json.dumps(args)

def set_winning_combos():
    winning_combinations = [
        [0, 1, 2],
        [1, 2, 3],
        [4, 5, 6],
        [5, 6, 7],
        [8, 9, 10],
        [9, 10, 11],
        [12, 13, 14],
        [13, 14, 15],
        [0, 4, 8],
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
        [5, 9, 13],
        [6, 10, 14],
        [7, 11, 15],
        [0, 5, 10],
        [1, 6, 11],
        [4, 9, 14],
        [5, 10, 15],
        [2, 5, 8],
        [3, 6, 9],
        [6, 9, 12],
        [7, 10, 13]
    ]
    win_check = np.zeros((len(winning_combinations), board_size), dtype=np.uint8)
    counter = 0
    for row in win_check:
        row[winning_combinations[counter]] = 255
        counter += 1
    return win_check

def check_for_win():
    for player in range(1, TOTAL_PLAYERS+1):      
        matches = win_check & game_board == player
        is_winner = np.sum(np.sum(matches, axis=1) == 3)
        if is_winner:
            return player
    return None

def check_for_draw():
    return np.sum(game_board == 0) == 0

if not win_check:
    win_check = set_winning_combos()

if __name__ == "__main__":
    app.run()