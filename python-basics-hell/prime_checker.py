import math



number = int(input("Enter a number: "))

if number < 2:
     print(number, "is not a prime number")
else:
     for i in range(2, int(math.sqrt(number)) + 1):
          if number % i == 0:
               print(number, "is not a prime number")
               break
     else:
          print(number, "is a prime number")
