# this is an Fibonacci sequence program
n = int(input("Enter the number of terms: "))

first_term = 0
second_term = 1
count = 0
if n <= 0:
     print("Please enter a positive integer.")
elif n == 1:
     print("Fibonacci sequence upto", n, ":")
     print(first_term)   
else:
     print("Fibonacci sequence:")
     while count < n:
         print(first_term)
         nth_term = first_term + second_term
         # update values
         first_term = second_term
         second_term = nth_term
         count += 1
     