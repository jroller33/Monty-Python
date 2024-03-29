# sets are similar to lists and dictionaries
# use { }, are unordered (can't be indexed)
# it's faster to check if an item is part of a set using `in` operator, rather than a list
# sets CAN'T contain duplicate elements

def first_set():
    num_set = {1, 2, 3, 4, 5}
    print(3 in num_set)     # True
    
def add_remove():
    nums = {1, 2, 1, 3, 1, 4, 5, 6}
    print(nums)     # duplicates get removed automatically
    
    nums.add(-7)
    nums.remove(3)
    
    print(nums)
    print(len(nums))    # prints length of the set
    
# def combining_sets():
    # union operator ` | ` combines to form a new one containing items in either
    # intersection operator ` & ` gets items only in both
    # difference operator ` - ` gets items in the first set but not in the second
    # symmetric operator ` * ` gets items in either set but not both
    