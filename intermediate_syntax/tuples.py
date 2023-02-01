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
            print(f"{ str(i[0]) } is { str(i[1]) }")
    # output age of the contact: "{Name} is {age}"    
    
    