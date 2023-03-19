# data in dictionaries is in key-value pairs
# keys can't be duplicated
# keys must be any immutable datatype (numbers, bools, strings or tuples), but you can't use a list or a dict as the key

def first_dict():
    dict = {'one': 1, 'two': 2, 'three': 3}
    # print("four" in dict) # False

    # add key-value to the end of a dictionary
    dict["five"] = 5
    print(dict)

    # change a key's value in dict
    dict["two"] = 67
    print(dict)

    # remove key-value from dict
    del dict["one"]
    print(dict)

def iterating_over_dict():
    files = {"jpg": 10, "txt": 14, "csv": 12}
    for extension in files:
        print(extension) # prints each key

    # .items() accesses the value
    for ext, amount in files.items():
        print(f"There's {amount} files with {ext} extension")

    print(files.keys())
    print(files.values())

    for value in files.values():
        print(value)

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

# if you need to search for a specific element, use dictionaries and not lists

