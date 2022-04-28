# Lionel Lynch
# project.py

# Program description: Provided in README file (attacted)

import random # Import random module.

# This function check the users guess against the answer and determines 
# how many letters the guess and answer how in common at each indice.
def check_answer(guess, answer):
  index = 0
  hint = ""
  for letter in guess:
    if letter == answer[index]:
      hint += u"\N{check mark}"
    elif letter in answer:
      hint += "~"
    else:
      hint += "-"
    index += 1
  print(hint)
  return hint == u"\N{check mark}\N{check mark}\N{check mark}\N{check mark}\N{check mark}"

# Imports the wordbank file, which provides the program with a set of
# five letter words.
word_list = []
word_file = open("project_wordbank.txt")
for word in word_file:
  word_list.append(word.strip())

# Main Function
def main():
    # Generate random word from word list.
    answer = random.choice(word_list)
    print(answer)
    
    # Track the users number of guesses and whether the user has
    # gussed the correct answer.
    num_guesses = 0
    correct_answer = False

    # Runs the loop as long as the user has less than six guesses and has not guessed
    # the correct word.
    while num_guesses < 6 and not correct_answer:
        
        # Get input from user
        guess = input("Guess a five letter  word: ").title()

        # Ensure user only enters 5 letter words.
        if len(guess) > 5:
            print('You can only input five letter words')

        else:
            print(f'You guessed {guess}') # Print users guess.
            num_guesses += 1 # Track users guess throughout the loop.

            # Check users guess against answer.
            correct_answer = check_answer(answer, guess)

    # Exit loop and provide user with Win or lose message.
    if correct_answer:
        print(f'You Win! You guessed the right word in {num_guesses} trys.')
    else:
        print(f"""You've ran out of guesses, the answer was {answer}.""")

if __name__== '__main__':
    main()