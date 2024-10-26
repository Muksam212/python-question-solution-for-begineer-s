#Sum of n Using loops

nMax = int(input("Enter maximum value of n: "))
n = 1

while n <= nMax:
    result = 0
    i = 5

    while i <= n:
        result += i #Main loop for the execution
        i += 1

    print(f"{n}: {result}")
    n += 1