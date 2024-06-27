import random
from datetime import datetime
from prettytable import PrettyTable
import sys

#create a function to generate a random number between 1 and 6
def roll_dice():
    "This function will create a random value for the dice"
    return random.randrange(1,7)

#create a function to create the game board of the game
def generate_table(human_position, computer_position):
    "This function will create the game board"
    human = [" "] * 20
    computer = [" "] * 20
    for i in range(20):
        if i == 6 or i == 13:
            human[i] = "O"
            computer[i] = "O"
    try:
        if human_position != 0:
            human[human_position-1] = "X"
    except IndexError:
        human[19] = "X"

    try:
        if computer_position != 0:
            computer[computer_position-1] = "X"
    except IndexError:
        computer[19] = "X"

    board = PrettyTable()
    board.field_names = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    board.add_row(human)
    board.add_row(computer)
    print(board)
    
#creating and initializing variables 
is_human_in_game = False
is_computer_in_game = False
human_position = 0
computer_position = 0
computer_message = ""
human_message = ""
computer_moves = 0
human_moves = 0
num_of_bh_hits_human = 0
num_of_bh_hits_computer = 0

#main program
#get the player name 
name = str(input("Enter your name here : "))
#give some details of the game
print("Hi",name,"welcome to the 20 x 2 game")
print("You will play against the computer.The first one who reach or pass the 20th block will win the game.\n")
while True:
    input("Press enter to roll the dice \n")
    is_diced_rolled_in_human_selection = False
    is_diced_rolled_in_computer_selection = False
    #assign the roll_dice function to variables
    dice_value_human = roll_dice()
    dice_value_computer = roll_dice()
    #check human
    if is_human_in_game == False:
        if dice_value_human == 6:
            is_human_in_game = True
            human_position = 0
            is_diced_rolled_in_human_selection = True
            human_message = f"Human dice roll is 6 and can start the game"
        else:
            human_message = f"Human dice roll is {dice_value_human} and cannot start the game"
    #check computer
    if is_computer_in_game == False:
        if dice_value_computer == 6:
            is_computer_in_game = True
            computer_position = 0
            is_diced_rolled_in_computer_selection = True
            computer_message = f"Computer dice roll is 6 and can start the game"
        else:
            computer_message = f"Computer dice roll is {dice_value_computer} and cannot start the game"
    #human turn
    if is_human_in_game == True:
        if is_diced_rolled_in_human_selection == False:
            human_position += dice_value_human // 2
            if (dice_value_human != 1):
                human_moves+=1
            if human_position == 7 or human_position == 14:
                num_of_bh_hits_human+=1
                human_position = 1
                human_message = f"Human dice roll is {dice_value_human} and hit a black hole"
            else:
                if human_position >= 20:
                    human_message = f"Human dice roll is {dice_value_human} and current location is 20""(Winner)"
                    computer_message = f"Computer dice roll is {dice_value_computer} and current location is {computer_position}"
                    generate_table(human_position, computer_position)
                    print(human_message)
                    print(computer_message)
                    break
                else:
                    human_message = f"Human dice roll is {dice_value_human} and current location is {human_position}"
    #computer turn
    if is_computer_in_game == True:
      if is_diced_rolled_in_computer_selection == False:
          computer_position += dice_value_computer // 2
          if (dice_value_computer != 1):
              computer_moves+=1
          if computer_position == 7 or computer_position == 14:
              num_of_bh_hits_computer+=1
              computer_position = 1
              computer_message = f"Computer dice roll is {dice_value_computer} and hit a black hole"
          else:
              if computer_position >= 20:
                  computer_message = f"Computer dice roll is {dice_value_computer} and current location is 20""(Winner)"
                  generate_table(human_position, computer_position)
                  print(human_message)
                  print(computer_message)
                  break
              else:
                  computer_message = f"Computer dice roll is {dice_value_computer} and current location is {computer_position}"

    generate_table(human_position, computer_position)
    print(human_message)
    print(computer_message,"\n")
   
#create a function for record game details to a text file
def text_file():
    "This function will create a text file based on the current date and time for game sessions"
    now_time = datetime.now()
    date = now_time.strftime("%Y_%m_%d_%H_%M")
    # above date will return as YYYY_M_D_H_M format
    file_name = 0
    file_name = open(date + ".txt","w")
    #human win
    if human_position >= 20:
        file_name.write("Human\n")
        file_name.write(f"Total moves {human_moves}\n")
        file_name.write(f"Black hole hits {num_of_bh_hits_human}\n")
        file_name.write("Won the game\n\n")
        file_name.write("Computer\n")
        file_name.write(f"Total moves {computer_moves}\n")
        file_name.write(f"Black hole hits {num_of_bh_hits_computer}\n")
        file_name.write("Lost the game\n")
    #computer win
    elif computer_position >= 20:
        file_name.write("Computer\n")
        file_name.write(f"Total moves {computer_moves}\n")
        file_name.write(f"Black hole hits {num_of_bh_hits_computer}\n")
        file_name.write("Won the game\n\n")
        file_name.write("Human\n")
        file_name.write(f"Total moves {human_moves}\n")
        file_name.write(f"Black hole hits {num_of_bh_hits_human}\n")
        file_name.write("Lost the game")
    else:
        None
    return
#call the function and create the text file
text_file()
sys.exit()
