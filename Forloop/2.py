#Sum of odd number using loops

nMax = int(input("Enter a maximum number: "))
n = 1

while n <= nMax:
    result = 0
    i = 1

    while i <= n:
        result += i #Main loop for the execution
        i += 2 #Since we are doing the odd

    print(f"{n}: {result}")
    n += 2