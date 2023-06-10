def sublist(lst, start, end):
    sub_list = lst[start:end:2]
    return sub_list
lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start = 2
end = 9
sub_list = sublist(lst, start, end)
print(sub_list)
