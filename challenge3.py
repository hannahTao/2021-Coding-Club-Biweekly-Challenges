import math

def calculator_functions(userInput):
  if userInput in ["add", "multiply", "divide"]:
    numOfNumbers = int(input("How many numbers do you want to " + userInput + "? "))
    for i in range(numOfNumbers):
      if i == 0:
        value = float(input("Input a number: "))
      else:
        if userInput == "add":
          value += float(input("Input a number: "))
        if userInput == "multiply":
          value *= float(input("Input a number: "))
        if userInput == "divide":
          value /= float(input("Input a number: "))
    return value

  elif userInput == "angles":
    conversion = input('Type "radians" to convert degrees to radians and "degrees" to convert radians to degrees: ')
    angleMeasure = float(input("Angle measure: "))
    if conversion == "degrees":
      return math.degrees(angleMeasure)
    if conversion == "radians":
      return math.radians(angleMeasure)

  elif userInput == "trig":
    trigFunction = input('Type "sin", "cos", "tan", "asin", "acos", or "acot": ')
    if trigFunction in ["sin", "cos", "tan"]:
      angleMeasure = float(input("Angle measure: "))
      if trigFunction == "sin":
        return math.sin(angleMeasure)
      if trigFunction == "cos":
        return math.cos(angleMeasure)
      if trigFunction == "tan":
        return math.tan(angleMeasure)
    elif trigFunction in ["asin", "acos", "acot"]:
      x = float(input("x: "))
      if trigFunction == "asin":
        return math.asin(x)
      if trigFunction == "acos":
        return math.acos(x)
      if trigFunction == "atan":
        return math.atan(x)

  elif userInput == "log":
    base = float(input("Base: "))
    x = float(input("x: "))
    return math.log(x, base)

  elif userInput == "Ln":
    x = float(input("x: "))
    return math.log(x)

  elif userInput == "x^y":
    x = float(input("x: "))
    y = float(input("y: "))
    return math.pow(x,y)

  elif userInput == "e^x":
    x = float(input("x: "))
    return math.exp(x)

  elif userInput == "sqrt":
    x = float(input("x: "))
    return math.sqrt(x)

  elif userInput == "remainder":
    x = float(input("x: "))
    y = float(input("y: "))
    return math.fmod(x,y)

  elif userInput == "factorial":
    x = int(input("x: "))
    return math.factorial(x)

  elif userInput == "gcd":
    x = int(input("x: "))
    y = int(input("y: "))
    return math.gcd(x,y)

  elif userInput == "hypotenuse":
    x = float(input("x: "))
    y = float(input("y: "))
    return math.hypot(x,y)
  
  elif userInput == 'more':
    output = 'You can type: \n"angles" to convert angle measures in degrees/radians\n"trig" for trig functions (mode radian)\n"log" to find logarithm of x to a base\n"Ln" to find natural logarithm of x\n"x^y" to raise x to the y power\n"e^x" to raise e to the x power\n"sqrt" to find square root of x\n"remainder" to find remainder when x/y, where x and y can be decimals\n"factorial" to find x factorial\n"gcd" to find gcd of integers x and y\n"hypotenuse" to find hypotenuse of a right triangle with legs of length x and y\n\nChoose one! '
    return output

print('Welcome to the calculator with many options!!')
print('Instructions: when prompted for input, type "add" "multiply" or "divide" (input negative numbers in "add" to subtract). Or, type "more" to see more options, or "done" when you are done with the calculator!\n')
userInput = input('What do YOU want to do with this calculator? ').strip()

possibleInputs = ['add', 'multiply', 'divide', 'angles', 'trig', 'log', 'Ln', 'x^y', 'e^x', 'sqrt', 'remainder', 'factorial', 'gcd', 'hypotenuse', 'more', 'done']

calcRunning = True
if userInput == 'done':
  print('Thank you for using my calculator!')
  calcRunning = False

while calcRunning:
  while userInput not in possibleInputs:
    userInput = input('Please type a valid input: ').strip()
    
  if userInput != 'done':
    print(calculator_functions(userInput))
    userInput = input('\nInput: ').strip()    # prompt for new input

  else:
    print('Thank you for using my calculator!')
    calcRunning = False
