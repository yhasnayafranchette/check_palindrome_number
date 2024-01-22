# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.

#Make a function to check if a number is a palindrome
def is_palindrome(number):
    original_number = number
    reverse_number = 0

#Reverse the number and check if the original number is equal to the reversed number
    while number > 0:
        digit = number % 10
        reverse_number = reverse_number * 10 + digit
        number = number // 10

    if original_number == reverse_number:
        return True
    else:
        return False
    
#Check if the number is a palindrome and print
number_one = 121
if is_palindrome(number_one):
    print(f"original number {number_one}\nYes. given number is palindrome number\n")
else:
    print(f"original number {number_one}\nNo. given number is not palindrome number\n")

number_two = 125
if is_palindrome(number_two):
    print(f"original number {number_two}\nYes. given number is palindrome number\n")
else:
    print(f"original number {number_two}\nNo. given number is not palindrome number\n")