import random

# Task 1: Create a list containing the names of your 5 favorite fruits
word_list = ["Apple", "Orange", "Pear", "Watermelon", "Banana"]

# Task 2: Choose a random word from the list
word = random.choice(word_list)
print(word)

# Task 3: Ask the user for an input
guess = input("Enter a single letter!")
print(guess)

# Task 4: Check that the input is a single character and only alphabetical characters
if len(guess) <= 1 and ((guess>='a' and guess<= 'z') or (guess>='A' and guess<='Z')):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")