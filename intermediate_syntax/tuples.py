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
    

    
    