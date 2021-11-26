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


