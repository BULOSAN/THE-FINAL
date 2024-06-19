# PYTHON PROJECTS:

#1 Number Guessing Game

import random

def number_guessing_game():
    range = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("It's a Number Guessing Game!")

    while not guessed_correctly:
        try:
            guess = int(input("Give a shot: "))
            attempts += 1

            if guess < range:
                print("too low")
            elif guess > range:
                print("too high.")
            else:
                guessed_correctly = True
                print(f"Correct!")
        except ValueError:
            print("Please enter a valid number.")

number_guessing_game()

print()
print()

# 2 General Knowledge Quiz

import random

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

def load_questions():
    questions = [
        Question("What is the capital of France?", "Paris"),
        Question("What is the value of x in x^2-20x+100", "10"),
        Question("What is the largest organ in our body'?", "Skin"),
        Question("What is the largest planet in our solar system?", "Jupiter"),
        Question("What is the smallest unit of matter?", "Atom"),
        Question("Who painted the Mona Lisa?", "Leonardo da Vinci"),
        Question("What is the chemical symbol for gold?", "Au"),
        Question("What is the capital city of the Israel", "Jerusalem"),
        Question("What is the hardest natural substance on Earth?", "Diamond"),
        Question("Who developed the theory of relativity?", "Albert Einstein"),
        Question("What is the main ingredient in sushi?", "Rice"),
        Question("What is 1/2 + 2/4 + 3/6 + 4/8", "2"),
        Question("Who was the first person to walk on the Moon?", "Neil Armstrong"),
        Question("Who wrote Romeo and Juliet?", "William Shakespeare"),
        Question("What is the capital city of the Canada", "Ottawa"),
        Question("What is the smallest country in the world?", "Vatican City"),
        Question("What is the boiling point of water in Celsius?", "100 Degree Celsius"),
        Question("What is the longest river in the world?", "Nile"),    
        Question("What is the capital city of the Thailand", "Bangkok"),
        Question("How many continents are there?", "7"),        
        Question("What gas do plants absorb from the atmosphere?", "Carbon Dioxide"),        
        Question("What is the tallest mountain in the world?", "Everest"),
        Question("What is the capital city of the Puerto Rico", "San Juan"),
        Question("What is the largest city in China?", "Shanghai"),
        Question("What is the largest mammal in the world?", "Blue Whale"),
        Question("What is the capital city of the India", "New Delhi"),
        Question("How many colors are there in a rainbow?", "Seven"),
        Question("What is the largest ocean on Earth?", "Pacific"),
        Question("What is the first element on the periodic table?", "Hygrogen"),
        Question("What is the smallest prime number?", "One"),
        Question("How many planets are in the solar system?", "7"),
        Question("What is the value of x in x^2-4x+4", "2"),
        Question("How many sides does a hexagon have?", "6"),
        Question("What is the currency used in the Philippines", "Peso"),
        Question("What planet is known as the Red Planet?", "Mars"),
        Question("What is the largest bone in the human body?", "Femur"),
        Question("What is the capital city of Australia?", "Canberra"),
        Question("What is the fastest land animal?", "Cheetah"),
        Question("What is the currency of the United States?", "US Dollar"),
        Question("What is the capital city of the Russia", "Moscow"),
        Question("How many days are in a leap year?", "366 days"),
        Question("How many seconds are there in one hour?", "3600"),
        Question("What is the chemical symbol for oxygen?", "O"),
        Question("What is the largest country in the world by area?", "Russia"),
        Question("What is the national bird of the United States?", "Bald Eagle"),
        Question("What is the national bird of the Philippines?", "Philippine Eagle"),
        Question("What is the square root of 10,000,000,000?", "100,000"),
        Question("What is the value of ln(e)", "1"),
        Question("What is the capital city of the Philippines", "Manila"),
        Question("What is the value of x in x^2-2x+1", "1"),

                 ]
    while len(questions) < 50:
        questions.extend(questions[:50-len(questions)])
    
    return questions

def quiz():
    questions = load_questions()
    random.shuffle(questions)
    score = 0
    user_answers = []

    print("Welcome to the General Knowledge Quiz!")

    for i, question in enumerate(questions):
        print(f"Question {i + 1}: {question.prompt}")
        user_answer = input("Your answer: ").strip()
        user_answers.append((question.prompt, user_answer, question.answer))

        if user_answer.lower() == question.answer.lower():
            score += 1
            print("Awesome!\n")
        else:
            print(f"Incorrect. Correct answer: {question.answer}\n")

    print(f"Quiz complete! You got {score} out of 50.")

if __name__ == "__main__":
    quiz()

print()
print()

# 3 Typing Master

import time

def typing_test():
    text_to_type = "Computer Programming"
    print("Guess by typing the text:")
    print(text_to_type)
    input("Press Enter to start")

    start_time = time.time()

    user_input = input("Type here: ")

    end_time = time.time()

    time_taken = end_time - start_time

    total_chars = len(text_to_type)
    correct_chars = sum(1 for i, c in enumerate(user_input) if i < len(text_to_type) and c == text_to_type[i])
    accuracy = (correct_chars / total_chars) * 100

    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Typed characters: {correct_chars}/{total_chars}")

if __name__ == "__main__":
    typing_test()

print()
print()

# 4 Measurement Converter

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def meters_to_miles(meters):
    return meters / 1609.34

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def feet_to_yards(feet):
    return feet / 3

def centimeters_to_inches(centimeters):
    return centimeters / 2.54

def show_menu():
    print("\nUnit Conversion Menu")
    print("1. Celsius to Fahrenheit")
    print("2. Meters to Miles")
    print("3. Kilograms to Pounds")
    print("4. Feet to Yards")
    print("5. Centimeters to Inches")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            celsius = float(input("Enter quantity in celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit}°F")
        elif choice == '2':
            meters = float(input("Enter quantity in meters: "))
            miles = meters_to_miles(meters)
            print(f"{meters} meters is {miles} miles")
        elif choice == '3':
            kilograms = float(input("Enter quantity in kilograms: "))
            pounds = kilograms_to_pounds(kilograms)
            print(f"{kilograms} kg is {pounds} lbs")
        elif choice == '4':
            feet = float(input("Enter quantity in feet: "))
            yards = feet_to_yards(feet)
            print(f"{feet} feet is {yards} yards")
        elif choice == '5':
            centimeters = float(input("Enter quantity in centimeters: "))
            inches = centimeters_to_inches(centimeters)
            print(f"{centimeters} cm is {inches} inches")
        elif choice == '6':
            print("Done!")
            break
        else:
            print("Invalid. Select only from 1 to 6.")

if __name__ == "__main__":
    main()

print()
print()

# 5 Rock Paper Scissors Game

import random

def play_round():
    number_to_guess = random.randint(1, 5)
    while True:
        try:
            player_guess = int(input("Guess a number between 1 and 5: "))
            if 1 <= player_guess <= 5:
                break
            else:
                print("Enter your number")
        except ValueError:
            print("Invalid. Select only between 1 and 5.")
    return player_guess == number_to_guess

def main():
    player_score = 0
    computer_score = 0
    round_number = 1
    
    print("Welcome to the Guess the number game where you'll guess a number between 1 and 5")
    print("First to win two rounds wins the game.")
    
    while player_score < 2 and computer_score < 2:
        print(f"\nRound {round_number}:")
        if play_round():
            player_score += 1
            print("Correct! You win this round.")
        else:
            computer_score += 1
            print("Incorrect. The computer wins this round.")
        
        round_number += 1
        print(f"Current Score -> You: {player_score}, Computer: {computer_score}")
    
    if player_score == 2:
        print("\nGreat!")
    else:
        print("\nYou lose. Better luck next time!")
    
if __name__ == "__main__":
    main()


print()
print()

# 6 Dice Rolling Simulator

import random

def roll_dice():
    return random.randint(1, 6)

def play_round(round_number):
    print(f"\nRound {round_number}:")

    input("Player 1, press Enter to roll the dice>")
    player1_roll = roll_dice()
    print(f"Player 1 rolled: {player1_roll}")

    input("Player 2, press Enter to roll the dice>")
    player2_roll = roll_dice()
    print(f"Player 2 rolled: {player2_roll}")

    if player1_roll > player2_roll:
        print("Player 1 wins this round!")
        return 1
    elif player2_roll > player1_roll:
        print("Player 2 wins this round!")
        return 2
    else:
        print("It's a tie! No one wins this round.")
        return 0

def main():
    player1_score = 0
    player2_score = 0
    round_number = 1
    
    print("It's a Dice Rolling Game")
    print("First player to win two rounds wins the game.")
    
    while player1_score < 2 and player2_score < 2:
        result = play_round(round_number)
        
        if result == 1:
            player1_score += 1
        elif result == 2:
            player2_score += 1
        
        round_number += 1
        print(f"Current Score -> Player 1: {player1_score}, Player 2: {player2_score}")
    
    if player1_score == 2:
        print("\nPlayer 1 won the game!")
    else:
        print("\nPlayer 2 won the game!")
    
if __name__ == "__main__":
    main()

print()
print()

# 7 Tic-Tac-Toe Game

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    players = [player1, player2]
    symbols = ["X", "O"]
    current_player = 0

    print_board(board)

    while True:
        print(f"{players[current_player]}'s turn ({symbols[current_player]})")
        while True:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                if board[row][col] == " ":
                    board[row][col] = symbols[current_player]
                    break
                else:
                    print("Cell already taken, try again.")
            except (ValueError, IndexError):
                print("Invalid, select only between 0 and 2.")

        print_board(board)

        if check_winner(board, symbols[current_player]):
            print(f"Congratulations {players[current_player]}! You win!")
            break

        if check_tie(board):
            print("It's a tie!")
            break

        current_player = 1 - current_player

if __name__ == "__main__":
    tic_tac_toe()

print()
print()

# 8 Password Generator

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the number of characters you want: "))
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()

print()
print()

# MATRIX:

# 1 Transpose the given input of 3x4 matrix:

def transpose_matrix(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    matrix = []
    print("Enter the elements of the 3x3 matrix row by row (separated by spaces):")
    for _ in range(3):
        row = list(map(int, input().split()))
        if len(row) != 3:
            print("Each row must have exactly 3 elements.")
            return
        matrix.append(row)
    
    print("\nOriginal Matrix:")
    print_matrix(matrix)

    transposed_matrix = transpose_matrix(matrix)
    
    print("\nTransposed Matrix:")
    print_matrix(transposed_matrix)

if __name__ == "__main__":
    main()

print()
print()

# 2 Find the sum of rows and columns of elements using numpy:

import numpy as np

matrix = np.array([[11, 24, 32],
                   [14, 35, 62],
                   [17, 82, 92]])

row_sums = np.sum(matrix, axis=1)

column_sums = np.sum(matrix, axis=0)

print("Matrix:")
print(matrix)

print("\nSum of rows:")
for i in range(3):
    print(f"Sum of row {i + 1}: {row_sums[i]}")

print("\nSum of columns:")
for i in range(3):
    print(f"Sum of column {i + 1}: {column_sums[i]}")

print()
print()

# 3 Find the sum of diagonal elements in a given matrix the manual way or NOT numpy way

import numpy as np

matrix = np.array([[1, 10, 11],
                   [48, 2, 65],
                   [77, 88, 3]])

main_diagonal_sum = np.trace(matrix)

anti_diagonal_sum = np.trace(matrix[:, ::-1])

print("Matrix:")
print(matrix)

print(f"\nSum of main diagonal elements: {main_diagonal_sum}")
print(f"Sum of anti-diagonal elements: {anti_diagonal_sum}")

