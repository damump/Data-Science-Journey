#Ask the user for a string and print out whether this string is a palindrome
#or not. (A palindrome is a string that reads the same forwards and backwards.)

check = input("Put in a word ")

if check.lower() == check[::-1].lower():
    print("This is a palindrone")
