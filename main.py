import numpy as np
import  random
list = [["-","2","-"],
        ["-","-","-"],
        ["-","-","-"],]
signs = ["X","O"]

for i in range(3):
    index = list[i].index("-")
    if index:
        list[i][index] = "2"
print(list)
# # problem with array condtional if an whole row not for element
# def is_winner(board):
#     for i in range(3):
#         if str(board[i]) == ["X","X","X"] or str(board[:,i]) == ["X","X","X"]:
#             print("you won")
#             return True
#         elif str(board[i]) == ["O", "O", "O"] or str(board[:,i]) == ["O", "O", "O"]:
#             print("you lost")
#             return True
#         elif board[1 ,1] == "O":
#             if board[0, 0] == "O" or board[0,2] == "O" and board[2, 0] == "O" or board[2,2] == "O":
#                 print("you lost")
#                 return True
#             elif board[0, 0] == "X" or board[0,2] == "X" and board[2, 0] == "X" or board[2,2] == "X":
#                 print("you lost")
#                 return True
#         else:
#             return False

def show_board(board):
    for row in board:
        print("  ".join(row))

def is_winner(list,player_sign):
    signs = ["X", "O"]
    for sign in signs:
        for i in range(3):
            if list[i] == [sign,sign,sign] \
                    or list[0][i] == sign and list[1][i] == sign and list[2][i] == sign:
                if sign == player_sign:
                    print("winner")
                    return True
                else:
                    print("lost")
                    return True
            if list[1][1] == sign:
                if list[0][0] == sign  and list[2][2] == sign \
                    or list[0][2] == sign  and list[2][0] == sign:
                        if sign == player_sign:
                            print("winner")
                            return True
                        else:
                            print("lost")
                            return True
            elif "-" not in list[0] and "-" not in list[1] and "-" not in list[2]:
                print("It is a draw!")
                return True
            else:
                return False


def game():
    game_continue = True
    turn = 1
    board = [["-","-","-"],
             ["-","-","-"],
             ["-","-","-"],]
    print("game start!!!")
    sign = input("which sign do you play with? X or O?").upper()
    if sign == "O":
        user_sign = "O"
        pc_sign = "X"
        turn = 2
    else:
        user_sign = "X"
        pc_sign = "O"
    show_board(board)
    while game_continue:
        if is_winner(board,user_sign):
            again = input("want to do it again? Y/N").upper()
            if again == "Y":
                game()
            else:
                game_continue = False
        elif turn % 2 != 0:
            choice = input("place your 'X' in board as 12 or 32(row 3 and column 2): ")
            if board[int(choice[0])-1][int(choice[1])-1] == "-":
                board[int(choice[0])-1][int(choice[1])-1] = user_sign
                turn += 1
                show_board(board)
            else:
                print("sorry but that box is not available pick anther one")
        else:
            # for i in range(3):
            #     index = list[i].index("-")
            #     if index:
            #         board[i][index] = "O"
            #         break
            #     else:
            #         continue
            random_row = random.randint(0, 2)
            random_col = random.randint(0, 2)
            if board[random_row][random_col] == "-":
                board[random_row][random_col] = pc_sign
                turn += 1
                show_board(board)
            else:
                print("please wait!")

game()