#1.1 Implement a recursive function to calculate the factorial of a given number
2. def recur_factorial(n):
if n == 1:
4
return n
5v else:
6
return n*recur_factorial(n-1)
7 # take input from the user
8 num = int(input("Enter a number: "))
9 # check is the number is negative
10 if num < 0:
11 print("Sorry, factorial does not exist for negative numbers")
12 elif num == 0:
13 print("The factorial of @ is 1")
14 else:
15 16
print("The factorial of", num, "is", recur_factorial(num))￼Not
