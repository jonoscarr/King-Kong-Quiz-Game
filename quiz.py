# import time library for better user experience
import time

# game function
def quiz_game():

# Shows the instructions for the game and proceeds to the first question
    instructions = '''
    ------------------------------Welcome to the King Kong Quiz Game!------------------------------

How to Play:

1. Answering Questions:
    - You will see a question with four multiple-choice options (A, B, C, D).
    - Type the letter corresponding to your answer and press Enter.

2. Scoring:
    - Correct answers earn you 1 point.
    - Incorrect answers will show the correct option.

3. Completion:
    - Your total score will be displayed at the end.
    - You can choose to play again if you wish.

Good luck and have fun!
'''

    print(instructions)

    score = 0 

    # Function to loop the input until the player enters a valid input(A, B, C or D)
    def answer_validator():

        while True:

            answer = input("Your answer (A, B, C, or D): ").strip().upper()

            if answer in ["A", "B", "C", "D",  "DECEMBER 2005", "WELLINGTON", "NEW ZEALAND", "WELLINGTON, NEW ZEALAND", "NAOMI WATTS", "NAOMI", "WATTS", "1933", "EMPIRE STATE BUILDING", "EMPIRE", "STATE"]:
                return answer
            else:
                print("Invalid input. Please enter A, B, C, D or choose an answer from one of the choices above.")

#----------------------------Prints all the questions with answer checker function----------------------------
    time.sleep(1)

    # Question 1
    print("When was the film King Kong(2005) released in the theaters?")
    print("--------------------------------------")
    print("A. December 2006")
    print("B. December 2005")
    print("C. January 2005")
    print("D. November 2005")
    print("--------------------------------------")
    Q1 = answer_validator()
    print("--------------------------------------")
    if Q1 == "B" or Q1 == "DECEMBER 2005":
        score += 1
        print("Correct!")
        print()
    else: 
        print("Wrong! It's B")
        print()

    # Question 2
    print("Where was the Skull Island portion of the movie filmed?")
    print("--------------------------------------")
    print("A. Sydney, Australia")
    print("B. Fiji")
    print("C. Wellington, New Zealand")
    print("D. Rio De Janeiro, Brazil")
    print("--------------------------------------")
    Q2 = answer_validator()
    print("--------------------------------------")
    if Q2 == "C" or Q2 == "WELLINGTON" or Q2 == "NEW ZEALAND" or Q2 == "WELLINGTON, NEW ZEALAND":
        score += 1
        print("Correct!")
        print()
    else: 
        print("Wrong! It's C")
        print()

    # Question 3
    print("Who plays the role of Ann Darrow, the female lead, in the 2005 film?")
    print("--------------------------------------")
    print("A. Naomi Watts")
    print("B. Kate Winslett")
    print("C. Rachel McAdams")
    print("D. Kirsten Dunst")
    print("--------------------------------------")
    Q3 = answer_validator()
    print("--------------------------------------")
    if Q3 == "A" or Q3 ==  "NAOMI WATTS" or Q3 == "NAOMI" or Q3 == "WATTS":
        score += 1
        print("Correct!")
        print()
    else: 
        print("Wrong! It's A")
        print()

    # Question 4
    print("What year is the King Kong(2005) film set in?")
    print("--------------------------------------")
    print("A. 1933")
    print("B. 1965")
    print("C. 1896")
    print("D. 1985")
    print("--------------------------------------")
    Q4 = answer_validator()
    print("--------------------------------------")
    if Q4 == "A" or Q4 == "1933":
        score += 1
        print("Correct!")
        print()
    else: 
        print("Wrong! It's A")
        print()

    # Question 5
    print("What famous landmark does King Kong climb in New York City?")
    print("--------------------------------------")
    print("A. World Trade Center")
    print("B. Brooklyn Bridge")
    print("C. Statue of Liberty")
    print("D. Empire State Building")
    print("--------------------------------------")
    Q5 = answer_validator()
    print("--------------------------------------")
    if Q5 == "D" or Q5 == "EMPIRE STATE BUILDING" or Q5 == "EMPIRE" or Q5 == "STATE":
        score += 1
        print("Correct!")
        print()
    else: 
        print("Wrong! It's D")  
        print()
#-------------------------------------------------------------------------------------------------------------------

# -------------------Displays stats for user and show their guesses and correct answers-----------------------
    print()
    print("----------------STATS-------------------")
    time.sleep(1)
    if score > 2:        
        print(f"Well done! your score is: {score}/5.")
    else:
        print(f"Better luck next time! your score is: {score}/5.")
    
    print(f"Your guesses: {Q1,Q2, Q3, Q4, Q5}")
    print('''
Answers:
          1. B. December 2005
          2. C. Wellington, New Zealand
          3. A. Naomi Watts
          4. A. 1933
          5. D. Empire State Building
          
          ''')

    play_again = input("Do you want to take the quiz again? ").strip().upper()


    if play_again == "YES" or play_again == "Y":
        quiz_game()
    else:
        pass
#-------------------------------------------------------------------------------------------------------------------

#--------------------------------------------Main routine goes here-------------------------------------------------

#----------------------------- Starts the program by asking the user if they want to play the quiz----------------------------
prompter = input("Do you want to play my quiz? ").strip().upper()

if prompter == "YES" or prompter == "Y":
    quiz_game()
else:
    print("Maybe next time?")
    pass

print()
time.sleep(1)

#-----------------Prompts user if they want to play again------------------

# ------------------------------------------------------------------------------------------------------#
    
