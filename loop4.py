'''
The rules for generating Collatz Sequence are:
If n is even:   n = n / 2
If n is odd:    n = 3n + 1
For example, if the starting number is 5 the sequence is:
5 -> 16 -> 8 -> 4 -> 2 -> 1
It has been proved for almost all integers, the repeated application of the above rule will result in a sequence that ends at 1.
Input format:
The input containing an integer 'n' which denotes the given number
Output format:
Print the numbers in the sequence and also print the number of times the rule has to be applied in order to reach 1.
Refer the sample output for formatting.
Sample Input:
5
Sample Output:
5
16
8
4
2
1
5
'''
def collatz_sequence(n):
    count = 0
    sequence = []
    
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:  # n is even
            n = n // 2
        else:           # n is odd
            n = 3 * n + 1
        count += 1
    
    sequence.append(1)  # Append the last number, which is 1
    return sequence, count

# Get input from the user
n = int(input("Enter a number: "))

# Generate the Collatz Sequence
sequence, steps = collatz_sequence(n)

# Print the sequence
for number in sequence:
    print(number)

# Print the number of steps
print(steps)
