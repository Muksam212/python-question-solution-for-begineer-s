num = int(input("Enter a number for factorial: "))

fact = 1

if num < 0:
    print("factorial number should be greater than 0")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        fact *= i
print(f"Factorial of number is: {fact}")