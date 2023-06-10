def sort_list(lst, key):
    l= len(lst)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if lst[j][key] > lst[j + 1][key]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


lst = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]
value= input("enter the value by which you want to sort the list")
if(value=='fruit'):
    sorted_list = sort_list(lst, "fruit")
else:
    sorted_list = sort_list(lst, "color")

print(sorted_list)
