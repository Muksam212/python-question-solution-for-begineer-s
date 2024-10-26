l1 = [1, 2, 3]
l2 = [2, 3, 4]

#Using list comprehension
intersection_element = [i for i in l1 if i in l2]
print(f"Common element: {intersection_element}")

#Using forloop
common_element = [] #Making empty list
for i in l1:
    if i in l2:
        common_element.append(i)

print(f"Common element: {common_element}")