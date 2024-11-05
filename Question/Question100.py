import numpy as np

# Question99: There are 300,000 comma-separated numbers in random_numbers.txt.
# Write a program to analyze these numbers and print the second smallest value,
# the second largest value, and the median value.
# The txt file is located at Z:\37_AI\question\random_numbers.txt

# Read the file and parse the numbers
with open(r'Z:\37_AI\question\random_numbers.txt', 'r') as file:
    numbers = file.read().split(',')

# Filter out any empty strings and convert to integers
numbers = list(map(int, filter(None, numbers)))
# Convert the list to a numpy array for easier manipulation
numbers = np.array(numbers)

# Sort the numbers
sorted_numbers = np.sort(numbers)

# Find the second smallest value
second_smallest = sorted_numbers[1]

# Find the second largest value
second_largest = sorted_numbers[-2]

# Find the median value
median_value = np.median(sorted_numbers)

# Print the results
print(f'Second smallest value: {second_smallest}')
print(f'Second largest value: {second_largest}')
print(f'Median value: {median_value}')