"""
Snake Ladder
"""
import random
import os
import time

# row where updates will be made on board
row = ["|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|"]
snake = [[98, 92, 62, 56, 51], [8, 53, 57, 15, 11]]
ladder = [[71, 52, 33, 9, 4], [97, 88, 85, 31, 14]]

players = dict()
player_values = list()

# this function runs when snake bites the player
def is_snake(row, current_player, current_player_sign, player_move, players):

    # update_game_board()
    current_move = players[current_player][1]
    for index, value in enumerate(snake[0]):
        if value == current_move:
            # current player's position is updated in the dictionary(players)
            players[current_player][1] = snake[1][index]
            player_move = players[current_player][1]
            print("Player {} bitten by the snake.\nDown to {}.".format(current_player, player_move))
            # pause the program for 3 seconds
            time.sleep(3)

# this function runs when player got the ladder
def is_ladder(row, current_player, current_player_sign, player_move, players):
    
    current_move = players[current_player][1]
    for index, value in enumerate(ladder[0]):
        if value == current_move:
            # current player's position is updated in the dictionary(players)
            players[current_player][1] = ladder[1][index]
            player_move = players[current_player][1]
            print("Player {} got the ladder.\nUp to {}.".format(current_player, player_move))
            # pause the program for 3 seconds
            time.sleep(3)

# Initial board is displayed on the screen before the game starts
def game_board(row, snake, ladder):
    # game title
    print("{0:^162}".format("SNAKE LADDER"))
    # instructions are printed out
    print("Intructions:\nSnake Bites: {}\tSnake Tail: {}, there respective values.".format(snake[0], snake[1]))
    print("Ladder Base: {}\t\tLadder Top: {}, there respective values.".format(ladder[0], ladder[1]))

    # new variable, for adding each updated block/cell on the board
    new_row = []

    step = 100
    # board top and center line is printed
    for board in range(1, 11):

        # top line loop
        horizontal_line = "   "
        for row_element in range(1, 162):
            horizontal_line += "-"
        print(horizontal_line)
        
        # adding numbering to each block/cell on the board
        for row_element in row:

            if row_element == " ":
                row_element = str(step)
                new_row.append("{0:^8}".format(row_element))
                step -= 1
            else:
                new_row.append("{0:^8}".format(row_element))

        # to reverse all the even rows on the baord, to make to look like snake ladder board
        center_line = ""
        if board % 2 == 0:
            for row_element in new_row[::-1]:
                center_line += row_element
            print(center_line)
        else:
            for row_element in new_row:
                center_line += row_element
            print(center_line)
        new_row = []

    # to print the last horizontal line
    horizontal_last = "   "
    for row_element in range(1, 162):
        horizontal_last += "-"
    print(horizontal_last)
    create_players(players, player_values)

# function runs to display the players's position on the board. 
def update_game_board(row, current_player, current_player_sign, player_move, players, snake, ladder):
    os.system("clear")
    # instructions are printed out
    print("{0:^162}".format("SNAKE LADDER"))
    print("Intructions:\nSnake Bites: {}\tSnake Tail: {}, there respective values.".format(snake[0], snake[1]))
    print("Ladder Base: {}\t\tLadder Top: {}, there respective values.".format(ladder[0], ladder[1]))

    new_row = []
    together = ""

    step = 100
    # board top and center line is printed
    for board in range(1, 11):

        # top line loop
        horizontal_line = "   "
        for row_element in range(1, 162):
            horizontal_line += "-"
        print(horizontal_line)

        # for particular block
        for row_element in row:

            # adding steps to the block and the signs of the players
            if row_element == " ":
                row_element = str(step)

                if player_move == row_element:
                    players[current_player][2] = player_move
                    together += current_player_sign

                # for updating the previous players sign with current one
                flag = current_player - 1
                while flag > 0:
                    if players[flag][2] == row_element:
                        together += players[flag][0]
                    flag -= 1
                step -= 1
            # updating all sign in the row element which is the block contents itself
            row_element += together
            new_row.append("{0:^8}".format(row_element))
            together = ""

        # current row is cleared up after the operation on that row
        center_line = ""

        # every random row is revered to look like a snake ladder board
        if board % 2 == 0:
            for row_element in new_row[::-1]:
                center_line += row_element
            print(center_line)
        else:
            for row_element in new_row:
                center_line += row_element
            print(center_line)
        new_row = []

    # to print the last horizontal line
    horizontal_last = "   "
    for row_element in range(1, 162):
        horizontal_last += "-"
    print(horizontal_last)

# ask the number of players want to play the game, minimum 1 player and maximum 4 players
def create_players(players, player_values):
    
    # setting the players and their marker
    while True:

        # getting total players want to play the game
        total_players = input("Choose total number of player (min 1 and max 4): ").strip()
        
        # if number of players does not meet the conditions
        if total_players not in ['1', '2', '3', '4']:
            print("Invalid input!")

        # if number of players meet the conditions
        else:
            print("Total players in the game {}".format(total_players))

            # players seting their marker/sign to display their position on the board
            total_players = int(total_players)
            for player_index in range(1, total_players + 1):
                while True:
                    set_marker = input("Now set your sign player {}:(alphabet only) ".format(player_index)).strip().upper()
                    if len(set_marker) != 1 or not(set_marker >= "A" and set_marker <= "Z"):
                        print("Invalid Sign choosen!")
                    else:
                        # marker set
                        player_values.append(set_marker)
                        # initial position of the player on the board is set to the zero
                        player_values.append(0)
                        # ever player last move is stored, to display along the current player's move
                        player_values.append("")
                        # player values as a list is stored in the dictionary(players) as its values. 
                        players[player_index] = player_values
                        player_values = []
                        break
            break
    # print(players)
    game_start(players)


def game_start(players):
    # way to start with first player
    from_Player = len(players) - (len(players) - 1)
    till_player = len(players) + 1

    flag = True
    while flag:

        for current_player in range(from_Player, till_player):

            current_player_sign = players[current_player][0]
            input("Player {} press [ENTER] to roll the dice: ".format(current_player, current_player_sign))

            # random library is used for dice work
            player_move = random.randint(1, 6)
            players[current_player][1] += player_move

            # checking for snake or ladder as player moves up
            if players[current_player][1] in snake[0]:
                is_snake(row, current_player, current_player_sign, player_move, players)
            if players[current_player][1] in ladder[0]:
                is_ladder(row, current_player, current_player_sign, player_move, players)

            if players[current_player][1] == 100:
                # casting to string(data type) to compare with number on the board
                player_move = str(players[current_player][1])
                update_game_board(row, current_player, current_player_sign, player_move, players, snake, ladder)
                print("Player {} won the game!".format(current_player))
                flag = False
                break
            elif players[current_player][1] < 100:

                # casting to string(data type) to compare with number on the board
                player_move = str(players[current_player][1])
                update_game_board(row, current_player, current_player_sign, player_move, players, snake, ladder)
                print("Player {} reach to {} position.".format(current_player, player_move))
                time.sleep(1)
            else:
                players[current_player][1] -= player_move
                # casting to string(data type) to compare with number on the board
                player_move = str(players[current_player][1])
                update_game_board(row, current_player, current_player_sign, player_move, players, snake, ladder)
                continue

# from this function game will be start
game_board(row, snake, ladder)