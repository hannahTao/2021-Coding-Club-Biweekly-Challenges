import random

print('Welcome to the random number guessing game! You have to try to guess the secret number, which is an integer randomly generated between the bounds you specify (inclusive). \n')

# Sets upper and lower bounds for randint, makes sure inputs are numbers
print('Set the bounds:')
lowerBound = input('What is the lower bound of the secret number? ')
while not lowerBound.isdigit():
  lowerBound = input('What is the lower bound of the secret number? ')
lowerBound = int(lowerBound)

upperBound = input('What is the upper bound of the secret number? ')
while not upperBound.isdigit():
  upperBound = input('What is the upper bound of the secret number? ')
upperBound = int(upperBound)

print('\nThe game has started!')
targetNumber = random.randint(lowerBound,upperBound)
triesUsed = 0
pastGuess = 0
gameRunning = True

while gameRunning:             # loop until user guesses the number
  guess = input('\nGuess a number between ' + str(lowerBound) + ' and ' + str(upperBound) + ': ')
  while not guess.isdigit():   # makes sure input is a number
    guess = input('Guess a number between ' + str(lowerBound) + ' and ' + str(upperBound) + ': ')
  guess = int(guess)
  
  if guess == pastGuess:      # repeated guess
    print('You guessed the same number!')

  else:
    pastGuess = guess
    if guess < targetNumber:
      triesUsed += 1
      print('Too low!')
      print('Tries used:', triesUsed)
    elif guess > targetNumber:
      triesUsed += 1
      print('Too high!')
      print('Tries used:', triesUsed)
    elif guess == targetNumber:
      triesUsed += 1
      print('You guessed it! You used ' + str(triesUsed) + ' guesses!')
      gameRunning = False
