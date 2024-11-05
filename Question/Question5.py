# Question5 This program has a bug that causes an error when executed.
# Please instruct GitHub Copilot to fix this bug.

# Variable definitions
a = 10
b = 0
c = 5
d = 2

# Complex calculation logic
result1 = a + c - d
result2 = a * d / c
result3 = (a + b) * (c - d)

# Calculation involving division by zero
if b != 0:
	result4 = a / b
else:
	result4 = None  # or handle the error as needed

# Output the results
print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)
print("Result 4:", result4)