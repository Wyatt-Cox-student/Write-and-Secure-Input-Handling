# The Incorrect Variable Usage: total += arr[i]
# The program assumes that every item in the array is a number. 
# If the array contains a string or another type of value, 
# the program could crash when trying to add it to the total.
items = [10, 20, 30, 40, 50]

def sum_array(arr):
    total = 0

    for i in range(len(arr)):
        if not isinstance(arr[i], (int, float)):
            raise ValueError("Array must contain only numbers")

        total += arr[i]

    return total

result = sum_array(items)

print("Sum of elements in the array:", result)
# The added validation checks whether each item is a number before adding it. 
# If an invalid value is found, 
# the program raises a clear error instead of trying to perform an incorrect calculation.