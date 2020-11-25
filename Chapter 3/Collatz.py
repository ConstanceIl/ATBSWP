# Define the function
def collatz(number):
  # If the number is even, perform float division. If the number is odd, multiply it 3 times and add 1
  if number % 2 == 0:
    result = number // 2
    print(result)
    return result
  else:
    result = 3 * number + 1
    print(result)
    return result

# Passive-aggresive function. Ask for user input
def f():
  inp = input('Please type a positive integer value: ')
  try:
    number = int(inp)
    print(number)
    if number < 1:
      print('I told you to type a POSITIVE integer value')
      f()
    else:
      while number != 1:
        number = collatz(number)
  except:
    print('I told you to type a positive INTEGER value')
    f()

f()
