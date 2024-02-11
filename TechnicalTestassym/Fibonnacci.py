# Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100.

def fibonacci_sequence(n):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print(fibonacci_sequence(100))






