import random

winning_numbers = set(random.sample(range(1, 49), 6))

guesses = set() 

guesses.add(int(input('Pick your first guess! Must be an integer number between 1 and 49: ')))
guesses.add(int(input('Pick your second guess! Must be an integer number between 1 and 49: ')))
guesses.add(int(input('Pick your third guess! Must be an integer number between 1 and 49: ')))
guesses.add(int(input('Pick your fourth guess! Must be an integer number between 1 and 49: ')))
guesses.add(int(input('Pick your fifth guess! Must be an integer number between 1 and 49: ')))
guesses.add(int(input('Pick your sixth guess! Must be an integer number between 1 and 49: ')))

matches = winning_numbers.intersection(guesses)

score = len(matches)

print('The winning numbers were', winning_numbers,'.')
print('You had', score, 'matches!')
