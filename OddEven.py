print("Problem 1 finding if a number is Odd or Even \n")

num1 = int(input("Enter a number: "))
mod = num1 % 2
if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")
   


print("\n Problem 2 check if a number is even or odd and Divisible by a number given \n") 

num = int(input("Give me a number to check: "))
check = int(input("Give me a number to divide by: "))

if num % 4 == 0:
    print(num, "is an even number")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")
    
if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)