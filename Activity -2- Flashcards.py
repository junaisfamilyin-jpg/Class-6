# 1) Create a class named `flashcard`.

# 2) Define the constructor `__init__(self, word, meaning)`:
#    a) Store the given `word` in `self.word`.
#    b) Store the given `meaning` in `self.meaning`.

# 3) Define the string method `__str__(self)`:
#    a) Return a formatted string in the form:
#       "word ( meaning )"
#    (This allows the object to be printed nicely.)

# 4) Create an empty list `flash` to store flashcard objects.

# 5) Print a welcome message for the flashcard application.

# 6) Start an infinite loop using `while(True)` to keep adding flashcards.

# 7) Inside the loop:
#    a) Take input from the user for the flashcard word and store it in `word`.
#    b) Take input from the user for the meaning and store it in `meaning`.

# 8) Create a new `flashcard` object using `word` and `meaning`
#    and add it to the list `flash` using `flash.append(...)`.

# 9) Ask the user if they want to add another flashcard:
#    a) Take input `option` (0 to continue, 1 to stop).
#    b) Convert it to integer using `int(...)`.

# 10) If `option` is 1 (true), stop the loop using `break`.
#     (If option is 0, the loop continues.)

# 11) After the loop ends, print "Your flashcards".

# 12) Use a `for` loop to iterate through each flashcard object in `flash`:
#     a) Print each flashcard using `print(">", i)`.
#     (This calls `__str__()` automatically for formatted output.)

class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word + " ( " + self.meaning + " )"


flash = []

print("Welcome to the flashcard application")

while (True):
    word = input("Enter the word: ")
    meaning = input("Enter the meaning: ")

    flash.append(flashcard(word, meaning))

    option = int(input("Enter 0 to add another flashcard, 1 to stop: "))

    if option == 1:
        break

print("Your flashcards")

for i in flash:
    print(">", i)
