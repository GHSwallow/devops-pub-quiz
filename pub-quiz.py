from inputimeout import inputimeout
import random
import questions


print("Welcome to the Pub Quiz!")

quiz_questions = questions.questions

users_score = 0

def generate_random_timeout(min=5, max=10):
    return random.randint(min, max)

for question in quiz_questions:
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    try: 
        user_answer = inputimeout("Your answer (A, B, C, D): ", generate_random_timeout()).strip().upper()
        if user_answer == question["answer"]:
            print("Correct!")
            users_score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")
    except: 
        time_over = 'Your time is over!'
        print("\n I'm sorry, you're just really slow at this \n") 


print(f"You scored {users_score}/{len(quiz_questions)}")

print("Thanks very much for playing the Pub Quiz!")