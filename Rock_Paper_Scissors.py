# Importing the random module

import random

# ASCII Art for Rock Paper Scissor

Rock = """
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """

Paper =  """
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

while True:

    game_images = [Rock,Paper,Scissors]
    user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scisssor. || Enter `quit` to exit\n")

    if user_choice == 'quit':
        print("Thank You for playing the game, Hope you enjoyed (:")
        break

    if int(user_choice) >= 3 or int(user_choice) < 0:
        print("You typed an invalid no., You Loose ):")
    else:
        print(game_images[int(user_choice)])

        computer_choice = random.randint(0,2)
        print(f"Computer choose : ")
        print(game_images[computer_choice])

        if int(user_choice) == 0 and computer_choice == 2:
            print("You win!!..(:(:")
        elif computer_choice == 0 and int(user_choice) == 2:
            print("You Loose..):")
        elif computer_choice > int(user_choice):
            print("You Loose..):")
        elif int(user_choice) > computer_choice:
            print("You Loose..):")
        elif computer_choice == int(user_choice):
            print("Its a draw")


