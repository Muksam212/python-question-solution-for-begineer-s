#Find the index of largest element in list
def largest_element(lst):
    largest = lst[0]

    out_index = 0

    for i, val in enumerate(lst):
        if val > largest:
            largest = val
            out_index = i
    return out_index

print(largest_element([1, 2, 3, 4, 5]))


#You can use another method

my_list = [1, 2, 3, 4]

'''
Lambda is an anonymous function that can takes any number of arguments
but has to be express on a single line

    Lambda argument: expression
'''
index_of_largest_element = max(range(len(my_list)), key = lambda i: my_list[i])
print(index_of_largest_element)