# tuples, lists and strings are sequences **
# strings are sequences of characters and immutable
# lists are sequences of any datatype and mutable
# tuples are sequences of any datatype and immutable


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
#     Tuples are used when you need to ensure that an element is in a certain position and will not change. order of the elements in a tuple can't be changed, so the position of the element in a tuple can have meaning. When a function returns multiple values, what gets returned is a tuple, with the return values as elements in the tuple. The order of the returned values is important, and a tuple ensures that the order isn’t going to change. Storing the elements of a tuple in separate variables is called unpacking (it works similiar to object destructuring in JavaScript) This allows you to take multiple returned values from a function and store each value in its own variable.

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