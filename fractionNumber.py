import math

number = int(input("Enter number: "))
digits = []

if number > 0:
  length = int(math.log10(number))
  for i in range(length, 0, -1):
    res = number - (number % (10 ** i))
    number = number % (10 ** i)
    digits.append(res)

  digits.append(number)
else:
  digits.append(0)	


print(digits)
