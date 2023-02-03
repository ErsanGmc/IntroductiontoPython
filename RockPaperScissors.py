#Import the random library
import random

#Add the code to create a list containing the three actions of the game.
action_list = ['rock', 'paper', 'scissors']

#Add the code to set the scores of players to 0
player1_score = 0
player2_score = 0

#Add the code to ask the user how many rounds they want to play: Usally 3 or 5
total_round = input("How many rounds do you want to play? ")

#Write a for loop and put the game inside
for i in range(int(total_round)):

  #Add the code to select a random action for each player
  player1_choice = random.choice(action_list)
  player2_choice = action_list[random.randint(0,2)]

  #Add the code to print the players choices
  print("Player1:", player1_choice)
  print("Player2:", player2_choice)

  #Add the tie condition
  if player1_choice == player2_choice:
    print("Tie! Both player chose same action.")

  #Add the remaining condition
  elif player1_choice == 'paper':
    if player2_choice == 'rock':
      print("Winner is: Player 1")
      player1_score +=1
    else:
      print("Winner is: Player 2")
      player2_score +=1

  elif player1_choice == 'rock':
    if player2_choice == 'paper':
      print("Winner is: Player 2")
      player2_score +=1
    else:
      print("Winner is: Player 1")
      player1_score +=1

  elif player1_choice == 'scissors':
    if player2_choice == 'paper':
      print("Winner is: Player 1")
      player1_score +=1
    else:
      print("Winner is: Player 2")
      player2_score +=1

  #print the score
  print("Score:", "Player1 =",player1_score, "Player2 =",player2_score)

