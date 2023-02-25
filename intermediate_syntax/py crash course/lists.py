# tuples, lists and strings are sequences **

#   ---  LISTS  ---

# lists are mutable in python
# ---  CRUD list methods:

def list_methods():
    # define a list
    fruits = ["Pineapple", "Apple", "Banana", "Orange", "Mango"]
    print(fruits)
    
    # add to the end of the list
    fruits.append("Kiwi")
    print(fruits)
    # add to the beginning of the list
    fruits.insert(0, "orange")
    print(fruits)
    # normally you'd either add to the beginning with insert(0) or the end with append()
    
    # remove the first occurance from the list
    fruits.remove("orange")
    print(fruits)
    
    fruits.pop(2) # removes the item at the index, also returns the item at that index, so you can store it in a variable if needed
    print(fruits)
    
    # replace an item in the list by its index
    fruits[2] = "Strawberry"
    print(fruits)
    
    
#            TUPLES              
    
# tuples are immutable in python, can be any datatype
# the position of the items in the tuple is important
# normally the location of an item in a tuple is used to identify it
tuple_example = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def convert_seconds(seconds):
    # 
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

def check_datatype_convert_seconds():
    result = convert_seconds(5000)
    print(type(result)) # <class 'tuple'>
    
# tuple methods: