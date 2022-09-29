import random

# Create a list containing the names of your 5 favorite fruits
word_list = ["Apple", "Orange", "Pear", "Watermelon", "Banana"]

word = random.choice(word_list)
#print(word)

guess = input("Enter a single letter!")
print(guess)

if len(guess) <= 1 and ((guess>='a' and guess<= 'z') or (guess>='A' and guess<='Z')):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")