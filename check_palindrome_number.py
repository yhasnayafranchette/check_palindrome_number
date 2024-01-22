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