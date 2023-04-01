# Start by asking for the number of numbers the user has
numbers = input("how many numbers do you have?\n")
# Convert the received number to an integer
int_number = int(numbers)
# Direct the user to start entering the numbers
print("Enter the", int_number, "numbers")
# Progress an empty list to start receiving the numbers
betting_numbers = []
# Write loop to receive the numbers one by one
count = 0
while count < int_number:
    betting_numbers.append(input())
    count += 1
# Ask the user for the number they wish to bet with
bet_number = input("Enter the number you wish to bet with\n")
# Write a loop to check if the number exists on the pool
# of the betting_numbers
for nambari in betting_numbers:
    if nambari == bet_number:
        print("Bet successful")
        break
