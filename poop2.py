'''
Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.
Input format:
The input containing an integer 'n' which denotes the given number.
Output format:
If the given number is factorial, print "Yes". Otherwise, print "No".
Refer the sample output for formatting.
Sample Input:
6
Sample Output:
Yes
'''
def is_factorial_number(n):
    if n < 1:
        return False  # Factorials are positive integers
    
    factorial = 1
    i = 1
    
    while factorial < n:
        i += 1
        factorial *= i
    
    return factorial == n

# Get input from the user
n = int(input("Enter a number: "))

# Check if the number is a factorial number
if is_factorial_number(n):
    print("Yes")
else:
    print("No")
