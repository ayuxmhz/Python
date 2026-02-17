# guessing
# secret_word = "money"
# guess = ""
# guessing_counts = 0
# guessing_limits = 3
# out_of_guesses = False

# while guess != secret_word and not (out_of_guesses):
#     if guessing_counts < guessing_limits:
#         guess = input("enter the guess: ")
#         guessing_counts += 1
#     else:
#         out_of_guesses = True

# if out_of_guesses:
#     print("Game Over, You lose!")
# else:
#     print("You have won the game")

# Guessing the number
secret_number = 69
guessing = " "
guessing_counts = 0
guessing_limits = 3
out_of_guesses = False

while guessing != secret_number and not (out_of_guesses):
    if guessing_counts < guessing_limits:
        guessing = int(input("Enter the number: "))
        guessing_counts += 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print("Game Over, You lose!")
else:
    print("You have won the game")
