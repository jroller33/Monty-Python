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
    
    fruits.pop(2) # removes the item at the index
    print(fruits)
    
    # replace an item in the list by its index
    fruits[2] = "Strawberry"
    print(fruits)
    
    
