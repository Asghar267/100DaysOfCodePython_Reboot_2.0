import random

print("Day 7 Tic Toe Game")

tic = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def display_place():  # Game Pattern
    print("\nTic Toe Game Places!")
    print("          -------------")
    print("         ", "|", tic[1], "|", tic[2], "|", tic[3], "|")
    print("          -------------")
    print("         ", "|", tic[4], "|", tic[5], "|", tic[6], "|")
    print("          -------------")
    print("         ", "|", tic[7], "|", tic[8], "|", tic[9], "|")
    print("          -------------\n")


def check_player1():     # Player 1 O  if condition is true player is winner

    if (tic[1] == "O" and tic[2] == "O" and tic[3] == "O"  # top-left top-middle top-right
            or tic[4] == "O" and tic[5] == "O" and tic[6] == "O"  # middle-left center middle-right
            or tic[7] == "O" and tic[8] == "O" and tic[9] == "O"  # bottom-right bottom-middle bottom-left
            or tic[1] == "O" and tic[4] == "O" and tic[7] == "O"  # left vertical
            or tic[3] == "O" and tic[5] == "O" and tic[8] == "O"  # Bottom-middle center Vertical
            or tic[3] == "O" and tic[6] == "O" and tic[9] == "O"  # Right Vertical
            or tic[1] == "O" and tic[2] == "O" and tic[3] == "O"  # Left top center bottom-right
            or tic[1] == "O" and tic[2] == "O" and tic[3] == "O"):  # Right-top center bottom-left
        return True


def check_player2():   # Player 2 O if condition is true player is winner
    if (tic[1] == "X" and tic[2] == "X" and tic[3] == "X"  # top-left top-middle top-right
            or tic[4] == "X" and tic[5] == "X" and tic[6] == "X"  # middle-left center middle-right
            or tic[7] == "X" and tic[8] == "X" and tic[9] == "X"  # bottom-right bottom-middle bottom-left
            or tic[1] == "X" and tic[4] == "X" and tic[7] == "X"  # left vertical
            or tic[3] == "X" and tic[5] == "X" and tic[8] == "X"  # Bottom-middle center Vertical
            or tic[3] == "X" and tic[6] == "X" and tic[9] == "X"  # Right Vertical
            or tic[1] == "X" and tic[2] == "X" and tic[3] == "X"  # Left top center bottom-right
            or tic[1] == "X" and tic[2] == "X" and tic[3] == "X"):  # Right-top center bottom-left
        return True


def check_input(inp):  # Check Input is correct place number or any other Character
    if not inp.isnumeric():  # Check input is number or other character
        return check_input(input("Wrong input Re Enter:"))
    else:  # if input is number then we check that place Filled or Not Exist
        inp = int(inp)
        if inp > 9:  # place not Exist
            return check_input(input("Place not Exist Re Enter:"))
        elif tic[inp] != inp:  # place is Already filled
            return check_input(input("Already Placed Re Enter:"))
        return int(inp)  # Correct input


def check_input_ai(inp):  # if AI chose Filled Place it will change
    if tic[inp] == inp:  # place is Already filled
        return inp
    return check_input_ai(random.randint(1, 9))


display_place()
print("Player 1 O")
print("Player 2 X")

players_op = input("OP 1:  Play with AI\n"
                   "OP 2:  Play With Human\n Option: ")
count = 1
for i in range(5):
    p1 = check_input(input("Chose Place for O Player 1: "))
    p2 = ''
    if count == 9:
        tic[p1] = "O"
        if check_player1():
            print("\n Congrats\n  Player 1 is Winner")
        else:
            print("Draw Game Over")
        display_place()
        break

    else:
        tic[p1] = "O"
        display_place()
        if check_player1():
            print("\n Congrats\n  Player 1 is Winner")
            display_place()
            break

        ply = "Player 2"
        if players_op == '1':  # Option 1 play with AI
            p2 = check_input_ai(random.randint(1, 9))
            print("Place for X AI: ", p2)
            ply = "AI"

        if players_op == '2':
            p2 = check_input(input("Chose Place for X Player 2: "))

        tic[p2] = "x"
        if check_player2():
            print(f"\n Congrats\n  {ply} is The Winner")
            break
        display_place()
        count += 2
