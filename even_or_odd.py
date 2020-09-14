##Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
##Hint: how does an even / odd number react differently when divided by 2?
##Extras:

#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num1 = int(input("Enter the even or odd number\n"))
num2 = int(input("Whatchu wanna divide by???\n"))

if num1 %2 ==0:
    print("this is an even number\n")
else:
    print("nah this is not even\n")
if num1 %num2 == 0:
    print("this is divisible by " + str(num2) + "\n")
else:
    print("this is not divisible by " + str(num2) + "\n")
if num1 %4 == 0:
    print(str(num1) + " Is a multiple of 4\n")
else:
    print(str(num1) + " Is not a multiple of 4\n")
