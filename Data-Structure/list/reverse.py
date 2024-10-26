def reverse_element(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

new_list = [1, 2, 3, 4]
obj = reverse_element(new_list)
print(obj)

print("=======================================")

def revList(lst):
    for i in range(len(lst) // 2):
        lst[i], lst[-1-i] = lst[-1-i], lst[i]

a = [1, 2, 3, 4]
revList(a)
print(a)