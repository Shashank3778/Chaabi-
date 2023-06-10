def get_file_type(extension_type_string, filenames):
    extension_type_list = extension_type_string.split(';')
    extension_type_dict = {}

    for item in extension_type_list:
        extension, file_type = item.split(',')
        extension_type_dict[extension] = file_type

    file_type_dict = {}

    for filename in filenames:
        file_extension = filename.split('.')[-1]
        file_type = extension_type_dict.get(file_extension, 'unknown')
        file_type_dict[filename] = file_type

    return file_type_dict

# Test the function
extension_type_string = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
filenames = ["abc.jpg", "xyz.xls", "text.csv", "123"]
file_type_dict = get_file_type(extension_type_string, filenames)
print(file_type_dict)
