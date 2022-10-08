import random

# Create a list containing the names of your 5 favorite fruits
word_list = ["Apple", "Orange", "Pear", "Watermelon", "Banana"]

# Choose a random word from the list
word = random.choice(word_list)

# Ask the user for an input
if __name__=="__main__":
    guess = input("Enter a single letter: ")

# Check that the input is a single character and only alphabetical characters
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
