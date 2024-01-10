#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

life_stage = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
'']


import random
chosen_word = random.choice(word_list)

key_word = []
life = -1

for i in range(0, len(chosen_word)):
  key_word.append("_")

while "_" in key_word: 
  word_check = 1
  guess_letter = input('Guess a letter: ').lower()
  
  for i in range(0, len(chosen_word)):
    
    if guess_letter == chosen_word[i]:
      key_word[i] = guess_letter
      word_check = 0

  output_word = ' '.join(key_word)
  life += word_check

  if life > 6:
    print('\n', '\n','Hangman died!', '\n')
    break

  else:
    print(life_stage[life])
    print(output_word, '\n')

if "_" in key_word:
  print('Game Over! Try to save the next hangman!', '\n')
else:
  print('Congratulations!','\n','You managed to save him!','\n','Can you save the next one?', '\n','...')