from getpass import getpass as input

intro = ("--------E P I C  🪨  📃 ✂️   B A T T L E-------- ")
print(intro.center(100))


print(
    "\033[35m",
    "\n---->it's AN 3 POINTS MATCH. The PLAYER WHO SCORES FIRST 3 POINTS shall win!!! <----",
    "\033[0m")

player1_score = 0
player2_score = 0
round = 0
# player1_score < 2 or player2_score < 2
while True:
  if player1_score == 3:
    print("\033[33m", "\n\n----->player 1 had reached at 3 points first. therefore player 1 WON 🥳🥳", "\033[0m")
    break
  elif player2_score == 3:
    print("\033[34m", "\n\n----->player 2 had reached at 3 points first. therefore player 2 WON 🥳🥳", "\033[0m")
    break

  round = round + 1
  print(f"\n\n------------> ROUND {round} <-------------------\n")

  print("select your move Rock, Paper or Scissor (pleas enter R, P or S)\n")
  player_1 = input("\033[33m"+"\nenter your move player 1 ---> "+"\033[0m")
  player_2 = input("\033[34m"+"\nenter your move player 2 ---> "+"\033[0m")

  if (player_1 == "R" or player_1 == "r") and (player_2 == "R"
                                               or player_2 == "r"):
    print("\033[31m", "\nit's an tie!!!!!😮😮 both picked rock", "\033[0m")
    print(
        f"player 1 score = {player1_score}\nplayer 2 score = {player2_score}")
  elif (player_1 == "R" or player_1 == "r") and (player_2 == "P"
                                                 or player_2 == "p"):
    print("\033[34m", "\nplayer 2 won as paper smash the rock!!!!!🥳🥳",
          "\033[0m")
    player2_score += 1
    print(
        f"player 1 score = {player1_score}\nplayer 2 score = {player2_score}")
  elif (player_1 == "R" or player_1 == "r") and (player_2 == "S"
                                                 or player_2 == "s"):
    print("\033[33m", "\nplayer 1 won as rock smash scisoor!!!!!🥳🥳", "\033[0m")
    player1_score += 1
    print(
        f"player 1 score = {player1_score}\nplayer 2 score = {player2_score}")

  elif (player_1 == "P" or player_1 == "p") and (player_2 == "R"
                                                 or player_2 == "r"):
    print("\033[33m", "\n PLAYER 1 won paper smash roch!!!!!🥳🥳", "\033[0m")
    player1_score += 1
    print(
        f"player 1 score = {player1_score}\nplayer 2 score = {player2_score}")
  elif (player_1 == "P" or player_1 == "p") and (player_2 == "P"
                                                 or player_2 == "p"):
    print("\033[31m", "\nit's an tie!!!!!😮😮 both pick paper", "\033[0m")
    print(
        f"player 1 score = {player1_score}\nplayer 2 score = {player2_score}")
  elif (player_1 == "P" or player_1 == "p") and (player_2 == "S"
                                                 or player_2 == "s"):
    print("\033[34m", "\n PLAYER 2 won as scissor smash paper!!!!!🥳🥳",
          "\033[0m")
    player2_score += 1
    print(
        f"player 1 score = {player1_score}\nplayer 2 score = {player2_score}")

  elif (player_1 == "S" or player_1 == "s") and (player_2 == "R"
                                                 or player_2 == "r"):
    print("\033[34m", "\nplayer 2 won as rock smash scissor!!!!!🥳🥳", "\033[0m")
    player2_score += 1
    print(
        f"player 1 score = {player1_score}\nplayer 2 score = {player2_score}")
  elif (player_1 == "S" or player_1 == "s") and (player_2 == "P"
                                                 or player_2 == "p"):
    print("\033[33m", "\nplayer 1 won as scissor smash paper!!!!!🥳🥳",
          "\033[0m")
    player1_score += 1
    print(
        f"player 1 score = {player1_score}\nplayer 2 score = {player2_score}")
  elif (player_1 == "S" or player_1 == "s") and (player_2 == "S"
                                                 or player_2 == "s"):
    print("\033[31m", "\nit's an tie!!!!!😮😮 both picked scissor", "\033[0m")
    print(
        f"player 1 score = {player1_score}\nplayer 2 score = {player2_score}")
  else:
    print("\033[31m", "\n\nERROR")
    print(
        "WRONG INPUT, make sure both players put (R, P or S or it's corresponding lowercase ONLY)",
        "\033[0m")
    print(
      f"player 1 score = {player1_score}\nplayer 2 score = {player2_score}")


print("\nthanks for playing the game😁😁")