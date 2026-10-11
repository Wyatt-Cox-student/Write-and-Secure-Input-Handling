# The Incorrect Variable is: total = 1, num_count = 1, and num = 1
# The total starts at 1 instead of 0, causing the final answer to be incorrect. 
# The program also doesn't check whether the user enters a valid number or a reasonable number of entries.
# Invalid input could cause the program to crash.

total = 0.0
num_count = 0
num = 0.0

try:
    num_count = int(input("How many numbers do you want to add? "))

    if num_count < 1 or num_count > 100:
        print("Please enter a number between 1 and 100.")

    else:
        for i in range(num_count):
            num = float(input("Enter number {}: ".format(i + 1)))

            if not (-1000000 <= num <= 1000000):
                raise ValueError("Number is outside the allowed range.")

            total += num

        print("The sum of the numbers you entered is:", total)

except ValueError:
    print("Invalid input. Please enter valid numbers.")

# Starting the total at 0 makes the calculation accurate. 
# The program also checks that the number of entries is 
# between 1 and 100 and that each value is within an allowed range. 
# The error handling prevents invalid input from crashing the program.