def find(list1, list2):
    x= set(list1)
    y = set(list2)

    common_elements = x.intersection(y)
    not_common= x.symmetric_difference(y)

    return list(common_elements), list(not_common)

#example
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common, not_common = find(list1, list2)
print("Common elements:", common)
print("Not common elements:", not_common)
