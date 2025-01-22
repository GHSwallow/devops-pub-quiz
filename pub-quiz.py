from inputimeout import inputimeout
import random
import questions
import time    

print("Welcome to the Pub Quiz!")

quiz_questions = questions.questions

users_score = 0
max_points = 0

def generate_random_timeout(min=5, max=10):
    return random.randint(min, max)

for question in quiz_questions:
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    try: 
        time_to_answer = generate_random_timeout()
        time_before = int(time.time())
        user_answer = inputimeout("Your answer (A, B, C, D): ", generate_random_timeout()).strip().upper() # Ensuring the input is uppercase for comparison
        time_after = int(time.time())
        if user_answer == question["answer"]:
            print("Correct!")
            users_score += time_to_answer - (time_after - time_before)
            max_points += time_to_answer
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")
    except: 
        time_over = 'Your time is over!'
        print("\nI'm sorry, you're just really slow at this") 
        
    print("Points = ", users_score)
    time.sleep(1)
    print()

print(f"You got {users_score}/{max_points} points")

print("Thanks very much for playing the Pub Quiz!")