from inputimeout import inputimeout
import random
import questions
import time    

# Welcome message for the quiz
print("Welcome to the Pub Quiz!")

# List of questions, options, and answers
quiz_questions = questions.questions

users_score = 0
max_points = 0

def generate_random_timeout(min=5, max=10):
    return random.randint(min, max)

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    # Get the user's answer
    try: 
        time_to_answer = generate_random_timeout()
        time_before = int(time.time())
        user_answer = inputimeout("Your answer (A, B, C, D): ", generate_random_timeout()).strip().upper() # Ensuring the input is uppercase for comparison
        time_after = int(time.time())
        # Check if the answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            users_score += time_to_answer - (time_after - time_before)
            max_points += time_to_answer
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")
    except: 
        time_over = 'Your time is over!'
        print("\nI'm sorry, you're just \033[3mreally\033[0m slow at this") 
        
    print("Points = ", users_score)
    time.sleep(1)
    print()

# Print score
print(f"You got {users_score}/{max_points} points")

# Goodbye message
print("Thanks very much for playing the Pub Quiz!")