def switch_key_value(dict1):
    swap_dict = dict([(value, key) for key, value in dict1.items()])
    return swap_dict


dict1 = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

swap_dict = switch_key_value(dict1)
print(swap_dict)
 
