# Given array of numbers
numbers = [10, 2, 8, 6, 7, 3]

# Bubble Sort implementation
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Print the sorted array
print("Sorted array in ascending order:", numbers)

#----
# Given array of numbers
numbers = [10, 2, 8, 6, 7, 3]

# Bubble Sort in descending order
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] < numbers[j + 1]:  # Only change: '<' instead of '>'
            # Swap
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Print the sorted array
print("Sorted array in descending order:", numbers)