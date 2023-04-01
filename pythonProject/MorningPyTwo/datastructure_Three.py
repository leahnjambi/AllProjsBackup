# Start by asking for the number of numbers the user has
numbers = input("how many numbers do you have?\n")
# Convert the received number to an integer
int_number = int(numbers)
# Direct the user to start entering the numbers
print("Enter the", int_number, "numbers")
# Progress an empty list to start receiving the numbers
user_numbers = []
count = 0
while count < int_number:
    user_numbers.append(input())
    count += 1
# write a loop to print the odd numbers
for num in user_numbers:
    # convert num to an integer
    converted_num = int(num)
    if (converted_num % 2) == 1:
        print(converted_num)

