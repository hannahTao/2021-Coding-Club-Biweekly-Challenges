import random

print('*** Welcome to the Multiplication Quiz! ***')
print('Now it\'s time to put your big brain skills to the test!')

print()
numQ = input('How many questions would you like your quiz to be (10 or more)? ')
while True:
  if not numQ.isdigit():
    numQ = input('Please input a nonnegative integer: ')
  elif int(numQ) < 10:
    numQ = input('Please input a number 10 or greater: ')
  else:
    break
numQ = int(numQ)

print('\nNow it\'s time to choose the difficulty for your quiz!')
digits1 = ''
while not digits1.isdigit():
  digits1 = input('How many digits would you like the first factor to have? ')
digits2 = ''

while not digits2.isdigit():
  digits2 = input('How many digits would you like the second factor to have? ')

digits1 = int(digits1) - 1    # this is the power 10 will be raised to
digits2 = int(digits2) - 1    # this is the power 10 will be raised to

print('\nGreat, now let\'s begin the quiz!')
numCorrect = 0

for question in range(numQ):
  num1 = random.randint(10**digits1, 10**(digits1+1)-1)
  num2 = random.randint(10**digits2, 10**(digits2+1)-1)
  product = num1 * num2

  userAnswer = input(str(num1) + ' x ' + str(num2) + ' = ')
  while not userAnswer.isdigit():
    userAnswer = input('Please input a nonnegative integer: ')
  
  if product == int(userAnswer):
    numCorrect += 1

print('\nLet\'s see your results!')
print('Questions correct:', numCorrect)
print('Questions wrong:', numQ-numCorrect)

bigBrainPoints = int(round(numCorrect/numQ, 2) * 100)
print('You got', str(bigBrainPoints) + ' Big Brain points! Be proud of yourself!!')

print('\nIf you can tell how the points were calculated, then +3.141592653589729 Big Brain points to you ;)')
