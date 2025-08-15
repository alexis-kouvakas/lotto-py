import random

def guess_input(guesses, attempts):
 if  attempts == 0: 
  return guesses
 guess = int(input('Pick your guess: '))
 if not (1 <= guess <= 49):
  print('Invalid input')
  guess_input(guesses, attempts)
 else:
  guesses.add(guess)
  guess_input(guesses, attempts-1)

winning_numbers = set(random.sample(range(1, 49), 6))
print('Guesses must be integer numbers between 1 and 49.') 
guesses = set()
attempts=6
guess_input(guesses, attempts)
    
     
matches = winning_numbers.intersection(guesses)
print('The winning numbers were', *winning_numbers,'.')
print('You had', len(matches) , 'matches!')
if len(matches) > 0: print('They were', *matches,'!')

