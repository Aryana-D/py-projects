import random

word = []
wrongLetter = []
guesses = []
guess = []
difficulty = []
right = []
wrong = []
easy = []
medium = []
hard = []
random.randint(0,14)
random.randint(0,11)
random.randint(0,9)

easy = ["dog", "cat", "red", "blue", "pink", "nail", "watch", "hat", "book", "jump",
        "life", "day", "year", "city"]
medium = ["water", "purple", "short", "shirt", "blank", "files", "shoes", "email", 
          "apple", "board", "glass"]
hard = ["journal", "pencil", "notebook", "pineapple", "vanilla", "tablet", "marker",
        "coffee", "twelve"]

art1 = ['''
--------
  |    |
       |
       |
       |
       |
=========''', '''
--------
  |    |
  o    |
       |
       |
       |
=========''', '''
--------
  |    |
  o    |
  |    |
       |
       |
=========''', '''
--------
  |    |
  o    |
 /|    |
       |
       |
=========''', '''
--------
  |    |
  o    |
 /|\   |
       |
       |
=========''', '''
--------
  |    |
  o    |
 /|\   |
 /     |
       |
=========''', '''
--------
  |    |
  o    |
 /|\   |
 / \   |
       |
=========''']

print("Hello! Welcome to Hangman.")
print("Do you want to play with 1 player or 2 players?\n")

choice = input("1 or 2\n")

if choice == "1":
  for _i in range(30):
     print()
  difficulty = input("Easy, Medium, Hard\n")
  if difficulty == "Easy" and difficulty == "easy" and difficulty == "EASY":
    random.randint(0,14)
    print(easy[random.randint(0,14)])

if choice == "2":
  word = input("Enter a word:\n")
  for _i in range(30):
    print()

for i in word:
  guesses.append("")
  
mistakes = 0
while "".join(guesses) != word:
  print(" ".join(guesses))
  guess = input("Guess a letter or word: ")
  if len(guess) == 1:
    # letter

    for i in range(len(guesses)):
      if guess == word[i]:
        guesses[i] = guess
        
    for _i in range(30):
     print()
  if not right and mistakes < len(art1)-1:
        mistakes += 1
        wrongLetter.append(guess)
  elif word == guess:
      guesses = []
      for i in guess:
        guesses.append(i)
  elif mistakes < len(art1)-1:
      mistakes += 1
      wrongLetter.append(guess)
if "".join(guesses) == word:
    print("You win! Good job, now go get a life or something.")
else:
   print(art1[mistakes])
   print("Wrong letters:")
   print(" ".join(wrongLetter))
