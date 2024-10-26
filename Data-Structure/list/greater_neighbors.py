def neighbor(lst):
    largest = lst[0]
    index = 0

    for i in range(1, len(lst) - 1):
        if lst[i - 1] + lst[i] + lst[i + 1] > largest:
            largest = lst[i - 1] + lst[i] + lst[i + 1]
            index = i
    return index

print(neighbor([1, 2, 3, 4]))