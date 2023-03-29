# a dictionary is a collection of objects in python
# they appear similar to user-defined objects in javascript, but work differently

# can be indexed using `[key]` (to get the key's value)
def first_dictionary():
    names = {
        "Dwight": "Schrute",
        "Michael": "Scott",
        "Jimothy": "Halpert"
    }
    print(names["Dwight"]) # Schrute
    print(names["Jimothy"]) # Halpert
    
# only immutable objects can be used as keys (lists and dictionaries are both mutable, so they can't be used as keys)
# strings, integers, booleans and other immutable types can be keys
    
def car_data():
    # take the key as input, output that key's value
    car = {
        'brand': 'Honda',
        'year': '2022',
        'color': 'blue'
    }
    key = input("Enter a key: ")
    print(f"The value of '{key}' is '{car[key]}'")

