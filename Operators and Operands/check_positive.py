#Checking positive negative or zero.

num = int(input("Enter a number: "))

#using ternary operators
results = "positive" if num > 0 else "negative" if num < 0 else "zero"

print(results)