# tuples are similar to lists, but they're ⚠️ IMMUTABLE ⚠️
# they use () instead of [] and can be indexed

def first_tuple():
    names = (
        "Michael",
        "Dwight",
        "Jim",
        "Pam",
        "Angela"
    )
    print(names[0])     # Michael
    
def different_types():
    list_example = ["Michael", "Jim", "Dwight"]     # mutable
    dict_example = {                                # mutable
        "Michael": "Scott",
        "Dwight": "Schrute",
        "Jim": "Halpert"
    }
    tuple_example = ("Michael", "Jim", "Dwight")    # IMMUTABLE
    tuple_without_parens = "Michael", "Jim", "Dwight"   # still immutable
    
def contact_list():
    contacts = [
        ('Michael', 52),
        ('Dwight', 41),
        ('Jim', 37),
        ('Pam', 34)
    ]
    # get a string as input
    name = input()
    
    # search for the name IN list of contacts
    for i in contacts:
        if name in i:
            print(f"{ str( i[0] ) } is { str( i[1] ) }")
        else:
            print("Not Found")
            
def tuple_unpacking():  # allows you to assign each item in a tuple to a variable
    numbers = (1,2,3)
    a, b, c = numbers
    print(a)
    print(b)
    print(c)
    
    # can also be used for a, b = b, a
    
    e, f, *g, h = [1, 2, 3, 4, 5, 6] #     *g takes all values leftover 
    print(e) # 1
    print(f) # 2
    print(g) # [3, 4, 5]
    print(h) # 6
    
def perimeter_area():
    side = int(input("Enter the side length of a square: "))
    p = side * 4
    a = side ** 2
    print(f"\nSquare's Perimeter: {p}\nSquare's Area: {a}\n")
    
perimeter_area()