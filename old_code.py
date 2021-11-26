@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@socketio.on('connect')
def new_player(auth):
    global current_players
    session["player"] = next(x for x in all if x not in current_players)
    current_players.append(session["player"])
    player_list = " ".join(current_players)   
    response = render_template("square.html", all_players=player_list)
    emit("player_update", response, broadcast=True)

@app.route('/')
def index():
    global current_color
    if len(current_players) < len(all):     
        if not current_color:
            current_color = colors[all.index(session["player"])]
        print(session["player"])
    return render_template("index.html", color_name=current_color)

@app.route('/correct', methods=['POST'])
def correct():
    return jsonify('', render_template("square.html", color_name=current_color))

@app.route('/change', methods=['POST'])
def change():
    global current_color
    if "player" in session:
        current_color = colors[all.index(session["player"])]
    else:
        current_color = ""
    return jsonify('', render_template("square.html", color_name=current_color))

@socket.on("disconnect")
def disconnect():
    current_players.remove(session["player"])

app.run(host='0.0.0.0')

def set_game_message(context):
    if context == "pregame":
        args = {
            "game_message_display": "flex", 
            "game_message_text": "Waiting for more players...", 
            "restart_button_display": "none"
        }
    elif context == "disconnect":
        args = {
            "game_message_display": "flex", 
            "game_message_text": "A player has disconnected", 
            "restart_button_display": "block"
        }
    elif context == "spectate":
        args = {
            "game_message_display": "none", 
            "game_message_text": "", 
            "restart_button_display": "none"
        }
    return render_template("game_message.html", args = args)

# context = "spectate" if session["player"] == "spectator" else "pregame"
# emit the proper game board to the current user (no broadcast). for all cases, convert numpy array into the necessary html and send that.
    # 3 cases:
        # 1. its a spectator going into active game. current game board should load for them
        # 2. player joining a lobby that still has not begun. default game board loaded
        # 3. player joining a lobby that has just started. default game board loaded
# emit the bottom of the page to the current user (no broadcast). each case is different however and will need a different context
    # 3 cases:
        # 1. its a spectator going into active game. spectator bottom should load only for them (emit no broadcast)
        # 2. player joining a lobby that has just started (emit with broadcast)
        # 3. player joining a lobby that still has not begun (emit no broadcast)
if session["player"] == "spectator":
    emit("load_bottom", set_bottom("spectate"))
elif len(current_players) == TOTAL_PLAYERS:
    emit("load_bottom", set_bottom("game"), broadcast=True)
else:
    emit("load_bottom", set_bottom("pregame"))