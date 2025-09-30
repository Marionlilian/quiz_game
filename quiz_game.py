def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    

    for key in questions:
        print(".....................................................................")
        print(key)

        for i in options[question_num - 1]:
            print(i)

        guess = input("Enter A, B, C, or D: ")
        guess = guess.upper()

        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)

        question_num += 1

    display_score(correct_guesses, guesses)



def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    print("........................................")
    print("RESULTS")
    print("...............................................")

    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("\nYour Score is: " + str(score) + "%")

    if score == 100:
        print("Excellent!")
    elif score >= 75:
        print("Good!")
    elif score >= 50:
        print("Average")
    elif score >= 25:
        print("Nice trial")
    else:
        print("Try Again")

   


def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False



questions = {
    "What is the largest desert in the world?: ": "C",
    "Who wrote Romeo and Juliet?: ": "B",
    "What is the chemical symbol for gold?: ": "C",
    "Who was the first President of the United States?: ": "C"
}


options = [
    ["A. Sahara", "B. Gobi", "C. Antarctic Desert", "D. Arabian"],
    ["A. William Wordsworth", "B. William Shakespeare", "C. Charles Dickens", "D. Jane Austen"],
    ["A. Ag", "B. Go", "C. Au", "D. Gd"],
    ["A. Thomas Jefferson", "B. Abraham Lincoln", "C. George Washington", "D. John Adams"],
]


new_game()

while play_again():
    new_game()

print("Byeeeee!")
