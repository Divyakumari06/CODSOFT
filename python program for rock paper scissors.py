import random

def rock_paper_scissors():

    user_score = 0
    computer_score = 0

    while True:
       
        computer_choice = random.randint(1, 3)

        user_choice = input("Enter your choice (rock = 1, paper = 2, scissors = 3): ")
  
        user_choice = int(user_choice)
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice - computer_choice) % 3 == 1:
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Your score: {user_score}, Computer score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ")

        if play_again.lower() != "yes":
            break

    print(f"Thanks for playing! Your final score is {user_score}, and the computer's final score is {computer_score}.")

rock_paper_scissors()