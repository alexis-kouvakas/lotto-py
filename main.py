import random

winning_numbers = set(random.sample(range(1, 49), 6))

print('Guesses must be integer numbers between 1 and 49.')
guesses = set()
for x in range(1, 7):
 x = x+1
 guesses.add(int(input('Pick your guess: ')))

matches = winning_numbers.intersection(guesses)
print('The winning numbers were', *winning_numbers,'.')
print('You had', len(matches) , 'matches!')
if len(matches) > 0: print('They were', *matches,'!')

