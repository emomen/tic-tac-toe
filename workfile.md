TODO
----
* figure out a screen

start screen (before 3 players have joined)

game_message_display="flex"
game_message_text="Waiting for more players..."
restart_button_display="none"

  <div class="game-message" id="gameMessage" style="display:{{ game_message_display }};">
    <div data-game-message-text>{{ game_message_text }}</div>
    <button id="restartButton" style="display:{{ restart_button_display }};">Restart</button>
  </div>

when to set the game board
when to set the bottom
when to redo game state

* connect
  * player
    * connecting before a game has enough players
    * connecting and being the last person needed for a game
  * spectator
    * connecting pregame or while a game is going (is there any difference between these?)
* disconnect
  * player
    * disconnecting pregame should just remove the player from the player_list
    * disconnecting during active game should shut down the game in a way where it can only be restarted by the restart button
  * spectator
    * should have no effect at all
* move
  * player
    * update the numpy game_board
    * check for win or draw (draw when all cells are non-zero)
    * broadcast to all users the htmlized version of the game board
      * if win or draw, update the bottom to indicate that a win or draw has occurred
  * spectator
    * N/A
* restart
  * player
    * should enter a period of waiting
    * waiting screen should be broadcast to all clients (even spectators)
    * redo game state at end of the waiting period
  * spectator
    * should never be able to see this button


* setting game board (dont do any emissions in the set_game_board function- do it elsewhere)
  1.) spectator - they should always get the current game board without broadcasting to anyone. game board should be unclickable for them
  2.) player pregame - they should just get the old board at the end of the previous game (or blank if there was no previous game)
  3.) player game - they should get the current game board (broadcasted to everyone when someone makes a move)

in connect function, we only worry about loading pregame boards and spectator boards who hop in mid-game. boards to players in game will be loaded by the move function and broadcasted to all clients.



* don't redo game state (new game) until 
  1.) you're at the waiting for players screen (may need to get there by pressing the restart button)
  2.) you have enough players for a new game (3 for now)
  3.) game in progress should be false during this waiting period

* figure out how to properly end game





(venv) pi@raspberrypi:/mnt/usb/tictactoe $ heroku logs --tail2021-11-27T09:36:50.615996+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:36:50.623629+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:37:19.673268+00:00 app[web.1]: [2021-11-27 09:37:19 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:162)
2021-11-27T09:37:19.673773+00:00 app[web.1]: [2021-11-27 09:37:19 +0000] [162] [INFO] Worker exiting (pid: 162)
2021-11-27T09:37:19.741718+00:00 app[web.1]: [2021-11-27 09:37:19 +0000] [171] [INFO] Booting worker with pid: 171
2021-11-27T09:37:20.599647+00:00 app[web.1]: * Serving Flask app 'app' (lazy loading)
2021-11-27T09:37:20.599679+00:00 app[web.1]: * Environment: production
2021-11-27T09:37:20.599680+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:37:20.599711+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:37:20.599726+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:37:20.604707+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:37:49.813018+00:00 app[web.1]: [2021-11-27 09:37:49 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:171)
2021-11-27T09:37:49.813499+00:00 app[web.1]: [2021-11-27 09:37:49 +0000] [171] [INFO] Worker exiting (pid: 171)
2021-11-27T09:37:49.882742+00:00 app[web.1]: [2021-11-27 09:37:49 +0000] [180] [INFO] Booting worker with pid: 180
2021-11-27T09:37:50.616849+00:00 app[web.1]: * Serving Flask app 'app' (lazy loading)
2021-11-27T09:37:50.616938+00:00 app[web.1]: * Environment: production
2021-11-27T09:37:50.616966+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:37:50.616996+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:37:50.617022+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:37:50.624084+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:38:18.000000+00:00 app[api]: Build started by user navenemom@gmail.com
2021-11-27T09:38:19.950822+00:00 app[web.1]: [2021-11-27 09:38:19 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:180)
2021-11-27T09:38:19.951357+00:00 app[web.1]: [2021-11-27 09:38:19 +0000] [180] [INFO] Worker exiting (pid: 180)
2021-11-27T09:38:20.011375+00:00 app[web.1]: [2021-11-27 09:38:20 +0000] [189] [INFO] Booting worker with pid: 189
2021-11-27T09:38:20.627889+00:00 app[web.1]: * Serving Flask app 'app' (lazy loading)
2021-11-27T09:38:20.628296+00:00 app[web.1]: * Environment: production
2021-11-27T09:38:20.628347+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:38:20.628390+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:38:20.628418+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:38:20.641217+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:38:25.000000+00:00 app[api]: Build failed -- check your build output: https://dashboard.heroku.com/apps/c9722380-7732-488f-9eb5-162e1ec5c777/activity/builds/0fd53cf4-1307-4a6b-a5c5-95b55e7436a4
2021-11-27T09:38:50.061792+00:00 app[web.1]: [2021-11-27 09:38:50 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:189)
2021-11-27T09:38:50.062297+00:00 app[web.1]: [2021-11-27 09:38:50 +0000] [189] [INFO] Worker exiting (pid: 189)
2021-11-27T09:38:50.129293+00:00 app[web.1]: [2021-11-27 09:38:50 +0000] [198] [INFO] Booting worker with pid: 198
2021-11-27T09:38:50.619794+00:00 app[web.1]: * Serving Flask app 'app' (lazy loading)
2021-11-27T09:38:50.619844+00:00 app[web.1]: * Environment: production
2021-11-27T09:38:50.619892+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:38:50.619930+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:38:50.619957+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:38:50.626983+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:39:20.236290+00:00 app[web.1]: [2021-11-27 09:39:20 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:198)
2021-11-27T09:39:20.236810+00:00 app[web.1]: [2021-11-27 09:39:20 +0000] [198] [INFO] Worker exiting (pid: 198)
2021-11-27T09:39:20.318699+00:00 app[web.1]: [2021-11-27 09:39:20 +0000] [207] [INFO] Booting worker with pid: 207
2021-11-27T09:39:20.701494+00:00 app[web.1]: * Serving Flask app 'app' (lazy loading)
2021-11-27T09:39:20.701547+00:00 app[web.1]: * Environment: production
2021-11-27T09:39:20.701596+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:39:20.701633+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:39:20.701660+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:39:20.726469+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:39:50.367857+00:00 app[web.1]: [2021-11-27 09:39:50 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:207)
2021-11-27T09:39:50.368376+00:00 app[web.1]: [2021-11-27 09:39:50 +0000] [207] [INFO] Worker exiting (pid: 207)
2021-11-27T09:39:50.431104+00:00 app[web.1]: [2021-11-27 09:39:50 +0000] [216] [INFO] Booting worker with pid: 216
2021-11-27T09:39:50.769747+00:00 app[web.1]: * Serving Flask app 'app' (lazy loading)
2021-11-27T09:39:50.769813+00:00 app[web.1]: * Environment: production
2021-11-27T09:39:50.769861+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:39:50.769898+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:39:50.769925+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:39:50.776901+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:40:04.000000+00:00 app[api]: Build started by user navenemom@gmail.com
2021-11-27T09:40:20.473893+00:00 app[web.1]: [2021-11-27 09:40:20 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:216)
2021-11-27T09:40:20.474374+00:00 app[web.1]: [2021-11-27 09:40:20 +0000] [216] [INFO] Worker exiting (pid: 216)
2021-11-27T09:40:20.534784+00:00 app[web.1]: [2021-11-27 09:40:20 +0000] [225] [INFO] Booting worker with pid: 225
2021-11-27T09:40:20.892569+00:00 app[web.1]: * Serving Flask app 'app' (lazy loading)
2021-11-27T09:40:20.892600+00:00 app[web.1]: * Environment: production
2021-11-27T09:40:20.892602+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:40:20.892632+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:40:20.892693+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:40:20.899853+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:40:34.377919+00:00 app[api]: Release v5 created by user navenemom@gmail.com
2021-11-27T09:40:34.377919+00:00 app[api]: Deploy f7bee2dd by user navenemom@gmail.com
2021-11-27T09:40:36.095352+00:00 heroku[web.1]: Restarting
2021-11-27T09:40:36.107457+00:00 heroku[web.1]: State changed from up to starting
2021-11-27T09:40:37.506769+00:00 heroku[web.1]: Stopping all processes with SIGTERM
2021-11-27T09:40:37.555786+00:00 app[web.1]: [2021-11-27 09:40:37 +0000] [4] [INFO] Handling signal: term
2021-11-27T09:40:39.655022+00:00 heroku[web.1]: Starting process with command `gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 application:app`
2021-11-27T09:40:40.513557+00:00 app[web.1]: [2021-11-27 09:40:40 +0000] [4] [INFO] Starting gunicorn 20.1.0
2021-11-27T09:40:40.513974+00:00 app[web.1]: [2021-11-27 09:40:40 +0000] [4] [INFO] Listening at: http://0.0.0.0:34793 (4)
2021-11-27T09:40:40.514020+00:00 app[web.1]: [2021-11-27 09:40:40 +0000] [4] [INFO] Using worker: geventwebsocket.gunicorn.workers.GeventWebSocketWorker
2021-11-27T09:40:40.517239+00:00 app[web.1]: [2021-11-27 09:40:40 +0000] [11] [INFO] Booting worker with pid: 11
2021-11-27T09:40:40.876722+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:40:40.876730+00:00 app[web.1]: * Environment: production
2021-11-27T09:40:40.876730+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:40:40.876731+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:40:40.876732+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:40:40.895450+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:40:40.916869+00:00 heroku[web.1]: State changed from starting to up
2021-11-27T09:40:46.000000+00:00 app[api]: Build succeeded
2021-11-27T09:41:07.510242+00:00 heroku[web.1]: Error R12 (Exit timeout) -> At least one process failed to exit within 30 seconds of SIGTERM
2021-11-27T09:41:07.518219+00:00 heroku[web.1]: Stopping remaining processes with SIGKILL
2021-11-27T09:41:07.641398+00:00 heroku[web.1]: Process exited with status 137
2021-11-27T09:41:10.619543+00:00 app[web.1]: [2021-11-27 09:41:10 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:11)
2021-11-27T09:41:10.620184+00:00 app[web.1]: [2021-11-27 09:41:10 +0000] [11] [INFO] Worker exiting (pid: 11)
2021-11-27T09:41:10.674493+00:00 app[web.1]: [2021-11-27 09:41:10 +0000] [20] [INFO] Booting worker with pid: 20
2021-11-27T09:41:10.985820+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:41:10.985836+00:00 app[web.1]: * Environment: production
2021-11-27T09:41:10.985861+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:41:10.985895+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:41:10.985913+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:41:10.999058+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:41:20.812351+00:00 heroku[router]: at=error code=H12 desc="Request timeout" method=GET path="/" host=csub.herokuapp.com request_id=b0030269-dbef-49ed-bfab-d8df07fa06f7 fwd="174.134.134.150" dyno=web.1 connect=0ms service=30000ms status=503 bytes=0 protocol=https
2021-11-27T09:41:40.758134+00:00 app[web.1]: [2021-11-27 09:41:40 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:20)
2021-11-27T09:41:40.758630+00:00 app[web.1]: [2021-11-27 09:41:40 +0000] [20] [INFO] Worker exiting (pid: 20)
2021-11-27T09:41:40.815505+00:00 app[web.1]: [2021-11-27 09:41:40 +0000] [29] [INFO] Booting worker with pid: 29
2021-11-27T09:41:41.790343+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:41:41.790411+00:00 app[web.1]: * Environment: production
2021-11-27T09:41:41.790463+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:41:41.790499+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:41:41.790528+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:41:41.800959+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)














(venv) pi@raspberrypi:/mnt/usb/tictactoe $ heroku logs --tail2021-11-27T09:52:24.525332+00:00 app[web.1]: * Environment: production
2021-11-27T09:52:24.525382+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:52:24.525420+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:52:24.525449+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:52:24.532621+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:52:35.956790+00:00 heroku[router]: at=error code=H12 desc="Request timeout" method=GET path="/" host=csub.herokuapp.com request_id=936decf7-756a-4dc9-9811-6cc0fce77fc3 fwd="174.134.134.150" dyno=web.1 connect=0ms service=30000ms status=503 bytes=0 protocol=https
2021-11-27T09:52:38.801541+00:00 heroku[router]: at=error code=H12 desc="Request timeout" method=GET path="/" host=csub.herokuapp.com request_id=98ddbeb2-cdfb-43af-8975-5cc6e47a4095 fwd="174.134.134.150" dyno=web.1 connect=0ms service=30000ms status=503 bytes=0 protocol=http
2021-11-27T09:52:54.269007+00:00 app[web.1]: [2021-11-27 09:52:54 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:20)
2021-11-27T09:52:54.269521+00:00 app[web.1]: [2021-11-27 09:52:54 +0000] [20] [INFO] Worker exiting (pid: 20)
2021-11-27T09:52:54.324302+00:00 app[web.1]: [2021-11-27 09:52:54 +0000] [29] [INFO] Booting worker with pid: 29
2021-11-27T09:52:55.268234+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:52:55.268284+00:00 app[web.1]: * Environment: production
2021-11-27T09:52:55.268334+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:52:55.268371+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:52:55.268401+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:52:55.280399+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:53:09.826735+00:00 heroku[router]: at=error code=H12 desc="Request timeout" method=GET path="/favicon.ico" host=csub.herokuapp.com request_id=31b30c58-b590-4c9c-a4c6-2c6f29b91eb7 fwd="174.134.134.150" dyno=web.1 connect=0ms service=30000ms status=503 bytes=0 protocol=http
2021-11-27T09:53:24.438790+00:00 app[web.1]: [2021-11-27 09:53:24 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:29)
2021-11-27T09:53:24.439319+00:00 app[web.1]: [2021-11-27 09:53:24 +0000] [29] [INFO] Worker exiting (pid: 29)
2021-11-27T09:53:24.494888+00:00 app[web.1]: [2021-11-27 09:53:24 +0000] [38] [INFO] Booting worker with pid: 38
2021-11-27T09:53:24.846018+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:53:24.846029+00:00 app[web.1]: * Environment: production
2021-11-27T09:53:24.846065+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:53:24.846092+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:53:24.846115+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:53:25.187529+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:53:54.532993+00:00 app[web.1]: [2021-11-27 09:53:54 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:38)
2021-11-27T09:53:54.533495+00:00 app[web.1]: [2021-11-27 09:53:54 +0000] [38] [INFO] Worker exiting (pid: 38)
2021-11-27T09:53:54.588719+00:00 app[web.1]: [2021-11-27 09:53:54 +0000] [47] [INFO] Booting worker with pid: 47
2021-11-27T09:53:55.279093+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:53:55.279181+00:00 app[web.1]: * Environment: production
2021-11-27T09:53:55.279264+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:53:55.279331+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:53:55.279375+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:53:55.290927+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:54:24.678228+00:00 app[web.1]: [2021-11-27 09:54:24 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:47)
2021-11-27T09:54:24.678881+00:00 app[web.1]: [2021-11-27 09:54:24 +0000] [47] [INFO] Worker exiting (pid: 47)
2021-11-27T09:54:24.751083+00:00 app[web.1]: [2021-11-27 09:54:24 +0000] [56] [INFO] Booting worker with pid: 56
2021-11-27T09:54:25.249325+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:54:25.249352+00:00 app[web.1]: * Environment: production
2021-11-27T09:54:25.249366+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:54:25.249414+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:54:25.249416+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:54:25.254588+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:54:54.810782+00:00 app[web.1]: [2021-11-27 09:54:54 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:56)
2021-11-27T09:54:54.811263+00:00 app[web.1]: [2021-11-27 09:54:54 +0000] [56] [INFO] Worker exiting (pid: 56)
2021-11-27T09:54:54.865005+00:00 app[web.1]: [2021-11-27 09:54:54 +0000] [65] [INFO] Booting worker with pid: 65
2021-11-27T09:54:55.188511+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:54:55.188522+00:00 app[web.1]: * Environment: production
2021-11-27T09:54:55.188544+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:54:55.188584+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:54:55.188614+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:54:55.194842+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:55:24.923900+00:00 app[web.1]: [2021-11-27 09:55:24 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:65)
2021-11-27T09:55:24.924404+00:00 app[web.1]: [2021-11-27 09:55:24 +0000] [65] [INFO] Worker exiting (pid: 65)
2021-11-27T09:55:24.980114+00:00 app[web.1]: [2021-11-27 09:55:24 +0000] [74] [INFO] Booting worker with pid: 74
2021-11-27T09:55:25.305006+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:55:25.305018+00:00 app[web.1]: * Environment: production
2021-11-27T09:55:25.305051+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:55:25.305081+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:55:25.305100+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:55:25.318028+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:55:55.074885+00:00 app[web.1]: [2021-11-27 09:55:55 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:74)
2021-11-27T09:55:55.075515+00:00 app[web.1]: [2021-11-27 09:55:55 +0000] [74] [INFO] Worker exiting (pid: 74)
2021-11-27T09:55:55.148107+00:00 app[web.1]: [2021-11-27 09:55:55 +0000] [83] [INFO] Booting worker with pid: 83
2021-11-27T09:55:55.476796+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:55:55.476806+00:00 app[web.1]: * Environment: production
2021-11-27T09:55:55.476834+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:55:55.476869+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:55:55.476887+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:55:55.489765+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:56:07.539172+00:00 heroku[router]: at=error code=H12 desc="Request timeout" method=GET path="/" host=csub.herokuapp.com request_id=0787e37e-f04b-44c0-8dbf-e2b4fd97b53f fwd="174.134.134.150" dyno=web.1 connect=0ms service=30001ms status=503 bytes=0 protocol=https
2021-11-27T09:56:25.186409+00:00 app[web.1]: [2021-11-27 09:56:25 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:83)
2021-11-27T09:56:25.186945+00:00 app[web.1]: [2021-11-27 09:56:25 +0000] [83] [INFO] Worker exiting (pid: 83)
2021-11-27T09:56:25.245422+00:00 app[web.1]: [2021-11-27 09:56:25 +0000] [92] [INFO] Booting worker with pid: 92
2021-11-27T09:56:26.279716+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:56:26.279770+00:00 app[web.1]: * Environment: production
2021-11-27T09:56:26.279821+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:56:26.279858+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:56:26.279888+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:56:26.287212+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:56:37.791614+00:00 heroku[router]: at=error code=H12 desc="Request timeout" method=GET path="/favicon.ico" host=csub.herokuapp.com request_id=c5a7a94a-9717-4ea9-be7b-f0fdb489452f fwd="174.134.134.150" dyno=web.1 connect=0ms service=30000ms status=503 bytes=0 protocol=https
2021-11-27T09:56:55.282217+00:00 app[web.1]: [2021-11-27 09:56:55 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:92)
2021-11-27T09:56:55.282769+00:00 app[web.1]: [2021-11-27 09:56:55 +0000] [92] [INFO] Worker exiting (pid: 92)
2021-11-27T09:56:55.348880+00:00 app[web.1]: [2021-11-27 09:56:55 +0000] [101] [INFO] Booting worker with pid: 101
2021-11-27T09:56:56.285254+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:56:56.285288+00:00 app[web.1]: * Environment: production
2021-11-27T09:56:56.285289+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:56:56.285319+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:56:56.285340+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:56:56.292731+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:57:25.464491+00:00 app[web.1]: [2021-11-27 09:57:25 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:101)
2021-11-27T09:57:25.465027+00:00 app[web.1]: [2021-11-27 09:57:25 +0000] [101] [INFO] Worker exiting (pid: 101)
2021-11-27T09:57:25.519271+00:00 app[web.1]: [2021-11-27 09:57:25 +0000] [110] [INFO] Booting worker with pid: 110
2021-11-27T09:57:25.849957+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:57:25.849989+00:00 app[web.1]: * Environment: production
2021-11-27T09:57:25.849990+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:57:25.850011+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:57:25.850031+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:57:25.863271+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:57:55.626521+00:00 app[web.1]: [2021-11-27 09:57:55 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:110)
2021-11-27T09:57:55.627095+00:00 app[web.1]: [2021-11-27 09:57:55 +0000] [110] [INFO] Worker exiting (pid: 110)
2021-11-27T09:57:55.701003+00:00 app[web.1]: [2021-11-27 09:57:55 +0000] [119] [INFO] Booting worker with pid: 119
^C
(venv) pi@raspberrypi:/mnt/usb/tictactoe $ heroku logs --tail
2021-11-27T09:52:54.324302+00:00 app[web.1]: [2021-11-27 09:52:54 +0000] [29] [INFO] Booting worker with pid: 29
2021-11-27T09:52:55.268234+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:52:55.268284+00:00 app[web.1]: * Environment: production
2021-11-27T09:52:55.268334+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:52:55.268371+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:52:55.268401+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:52:55.280399+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:53:09.826735+00:00 heroku[router]: at=error code=H12 desc="Request timeout" method=GET path="/favicon.ico" host=csub.herokuapp.com request_id=31b30c58-b590-4c9c-a4c6-2c6f29b91eb7 fwd="174.134.134.150" dyno=web.1 connect=0ms service=30000ms status=503 bytes=0 protocol=http
2021-11-27T09:53:24.438790+00:00 app[web.1]: [2021-11-27 09:53:24 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:29)
2021-11-27T09:53:24.439319+00:00 app[web.1]: [2021-11-27 09:53:24 +0000] [29] [INFO] Worker exiting (pid: 29)
2021-11-27T09:53:24.494888+00:00 app[web.1]: [2021-11-27 09:53:24 +0000] [38] [INFO] Booting worker with pid: 38
2021-11-27T09:53:24.846018+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:53:24.846029+00:00 app[web.1]: * Environment: production
2021-11-27T09:53:24.846065+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:53:24.846092+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:53:24.846115+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:53:25.187529+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:53:54.532993+00:00 app[web.1]: [2021-11-27 09:53:54 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:38)
2021-11-27T09:53:54.533495+00:00 app[web.1]: [2021-11-27 09:53:54 +0000] [38] [INFO] Worker exiting (pid: 38)
2021-11-27T09:53:54.588719+00:00 app[web.1]: [2021-11-27 09:53:54 +0000] [47] [INFO] Booting worker with pid: 47
2021-11-27T09:53:55.279093+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:53:55.279181+00:00 app[web.1]: * Environment: production
2021-11-27T09:53:55.279264+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:53:55.279331+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:53:55.279375+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:53:55.290927+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:54:24.678228+00:00 app[web.1]: [2021-11-27 09:54:24 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:47)
2021-11-27T09:54:24.678881+00:00 app[web.1]: [2021-11-27 09:54:24 +0000] [47] [INFO] Worker exiting (pid: 47)
2021-11-27T09:54:24.751083+00:00 app[web.1]: [2021-11-27 09:54:24 +0000] [56] [INFO] Booting worker with pid: 56
2021-11-27T09:54:25.249325+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:54:25.249352+00:00 app[web.1]: * Environment: production
2021-11-27T09:54:25.249366+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:54:25.249414+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:54:25.249416+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:54:25.254588+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:54:54.810782+00:00 app[web.1]: [2021-11-27 09:54:54 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:56)
2021-11-27T09:54:54.811263+00:00 app[web.1]: [2021-11-27 09:54:54 +0000] [56] [INFO] Worker exiting (pid: 56)
2021-11-27T09:54:54.865005+00:00 app[web.1]: [2021-11-27 09:54:54 +0000] [65] [INFO] Booting worker with pid: 65
2021-11-27T09:54:55.188511+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:54:55.188522+00:00 app[web.1]: * Environment: production
2021-11-27T09:54:55.188544+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:54:55.188584+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:54:55.188614+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:54:55.194842+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:55:24.923900+00:00 app[web.1]: [2021-11-27 09:55:24 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:65)
2021-11-27T09:55:24.924404+00:00 app[web.1]: [2021-11-27 09:55:24 +0000] [65] [INFO] Worker exiting (pid: 65)
2021-11-27T09:55:24.980114+00:00 app[web.1]: [2021-11-27 09:55:24 +0000] [74] [INFO] Booting worker with pid: 74
2021-11-27T09:55:25.305006+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:55:25.305018+00:00 app[web.1]: * Environment: production
2021-11-27T09:55:25.305051+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:55:25.305081+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:55:25.305100+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:55:25.318028+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:55:55.074885+00:00 app[web.1]: [2021-11-27 09:55:55 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:74)
2021-11-27T09:55:55.075515+00:00 app[web.1]: [2021-11-27 09:55:55 +0000] [74] [INFO] Worker exiting (pid: 74)
2021-11-27T09:55:55.148107+00:00 app[web.1]: [2021-11-27 09:55:55 +0000] [83] [INFO] Booting worker with pid: 83
2021-11-27T09:55:55.476796+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:55:55.476806+00:00 app[web.1]: * Environment: production
2021-11-27T09:55:55.476834+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:55:55.476869+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:55:55.476887+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:55:55.489765+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:56:07.539172+00:00 heroku[router]: at=error code=H12 desc="Request timeout" method=GET path="/" host=csub.herokuapp.com request_id=0787e37e-f04b-44c0-8dbf-e2b4fd97b53f fwd="174.134.134.150" dyno=web.1 connect=0ms service=30001ms status=503 bytes=0 protocol=https
2021-11-27T09:56:25.186409+00:00 app[web.1]: [2021-11-27 09:56:25 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:83)
2021-11-27T09:56:25.186945+00:00 app[web.1]: [2021-11-27 09:56:25 +0000] [83] [INFO] Worker exiting (pid: 83)
2021-11-27T09:56:25.245422+00:00 app[web.1]: [2021-11-27 09:56:25 +0000] [92] [INFO] Booting worker with pid: 92
2021-11-27T09:56:26.279716+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:56:26.279770+00:00 app[web.1]: * Environment: production
2021-11-27T09:56:26.279821+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:56:26.279858+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:56:26.279888+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:56:26.287212+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:56:37.791614+00:00 heroku[router]: at=error code=H12 desc="Request timeout" method=GET path="/favicon.ico" host=csub.herokuapp.com request_id=c5a7a94a-9717-4ea9-be7b-f0fdb489452f fwd="174.134.134.150" dyno=web.1 connect=0ms service=30000ms status=503 bytes=0 protocol=https
2021-11-27T09:56:55.282217+00:00 app[web.1]: [2021-11-27 09:56:55 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:92)
2021-11-27T09:56:55.282769+00:00 app[web.1]: [2021-11-27 09:56:55 +0000] [92] [INFO] Worker exiting (pid: 92)
2021-11-27T09:56:55.348880+00:00 app[web.1]: [2021-11-27 09:56:55 +0000] [101] [INFO] Booting worker with pid: 101
2021-11-27T09:56:56.285254+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:56:56.285288+00:00 app[web.1]: * Environment: production
2021-11-27T09:56:56.285289+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:56:56.285319+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:56:56.285340+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:56:56.292731+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:57:25.464491+00:00 app[web.1]: [2021-11-27 09:57:25 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:101)
2021-11-27T09:57:25.465027+00:00 app[web.1]: [2021-11-27 09:57:25 +0000] [101] [INFO] Worker exiting (pid: 101)
2021-11-27T09:57:25.519271+00:00 app[web.1]: [2021-11-27 09:57:25 +0000] [110] [INFO] Booting worker with pid: 110
2021-11-27T09:57:25.849957+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:57:25.849989+00:00 app[web.1]: * Environment: production
2021-11-27T09:57:25.849990+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:57:25.850011+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:57:25.850031+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:57:25.863271+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:57:55.626521+00:00 app[web.1]: [2021-11-27 09:57:55 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:110)
2021-11-27T09:57:55.627095+00:00 app[web.1]: [2021-11-27 09:57:55 +0000] [110] [INFO] Worker exiting (pid: 110)
2021-11-27T09:57:55.701003+00:00 app[web.1]: [2021-11-27 09:57:55 +0000] [119] [INFO] Booting worker with pid: 119
2021-11-27T09:57:56.248973+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:57:56.248999+00:00 app[web.1]: * Environment: production
2021-11-27T09:57:56.249020+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:57:56.249031+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:57:56.249058+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:57:56.253924+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:58:25.800383+00:00 app[web.1]: [2021-11-27 09:58:25 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:119)
2021-11-27T09:58:25.801076+00:00 app[web.1]: [2021-11-27 09:58:25 +0000] [119] [INFO] Worker exiting (pid: 119)
2021-11-27T09:58:25.890264+00:00 app[web.1]: [2021-11-27 09:58:25 +0000] [128] [INFO] Booting worker with pid: 128
2021-11-27T09:58:26.441879+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:58:26.441896+00:00 app[web.1]: * Environment: production
2021-11-27T09:58:26.441938+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:58:26.441980+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:58:26.442011+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:58:26.449529+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:58:56.019910+00:00 app[web.1]: [2021-11-27 09:58:56 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:128)
2021-11-27T09:58:56.020428+00:00 app[web.1]: [2021-11-27 09:58:56 +0000] [128] [INFO] Worker exiting (pid: 128)
2021-11-27T09:58:56.077128+00:00 app[web.1]: [2021-11-27 09:58:56 +0000] [137] [INFO] Booting worker with pid: 137
2021-11-27T09:58:56.385510+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:58:56.385521+00:00 app[web.1]: * Environment: production
2021-11-27T09:58:56.385549+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:58:56.385571+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:58:56.385590+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:58:56.400729+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:59:26.126790+00:00 app[web.1]: [2021-11-27 09:59:26 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:137)
2021-11-27T09:59:26.127307+00:00 app[web.1]: [2021-11-27 09:59:26 +0000] [137] [INFO] Worker exiting (pid: 137)
2021-11-27T09:59:26.181273+00:00 app[web.1]: [2021-11-27 09:59:26 +0000] [146] [INFO] Booting worker with pid: 146
2021-11-27T09:59:26.539505+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:59:26.539521+00:00 app[web.1]: * Environment: production
2021-11-27T09:59:26.539552+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:59:26.539575+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:59:26.539602+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:59:26.545653+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T09:59:56.273658+00:00 app[web.1]: [2021-11-27 09:59:56 +0000] [4] [CRITICAL] WORKER TIMEOUT (pid:146)
2021-11-27T09:59:56.274179+00:00 app[web.1]: [2021-11-27 09:59:56 +0000] [146] [INFO] Worker exiting (pid: 146)
2021-11-27T09:59:56.328992+00:00 app[web.1]: [2021-11-27 09:59:56 +0000] [155] [INFO] Booting worker with pid: 155
2021-11-27T09:59:57.260815+00:00 app[web.1]: * Serving Flask app 'application' (lazy loading)
2021-11-27T09:59:57.260866+00:00 app[web.1]: * Environment: production
2021-11-27T09:59:57.260917+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2021-11-27T09:59:57.260954+00:00 app[web.1]: Use a production WSGI server instead.
2021-11-27T09:59:57.260985+00:00 app[web.1]: * Debug mode: off
2021-11-27T09:59:57.268295+00:00 app[web.1]: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
2021-11-27T10:00:22.843354+00:00 heroku[web.1]: State changed from up to down
2021-11-27T10:00:23.581098+00:00 heroku[web.1]: Stopping all processes with SIGTERM
2021-11-27T10:00:23.613454+00:00 app[web.1]: [2021-11-27 10:00:23 +0000] [4] [INFO] Handling signal: term
2021-11-27T10:00:22.730820+00:00 app[api]: Scaled to web@0:Free by user navenemom@gmail.com