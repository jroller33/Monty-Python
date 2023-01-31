# you can use `in` and `not in` with dictionaries just like lists

nums = {
    1: "one",
    2: "two",
    3: "three"
}

def in_notin():
    print(1 in nums)        # True
    print("three" in nums)  # False
    print(4 not in nums)    # True

# .get() method works like indexing, but if the key isn't
# in the dictionary, it returns a different value instead

def get_method():
    pairs = {
        1: "apple",
        "orange": [2, 3, 4],
        True: False,
        12: "True"
    }
    print(pairs.get("orange"))       # [2, 3, 4]
    print(pairs.get(7, 42))          # 42
    print(pairs.get(12345, "not found"))    # not found
    
# len() can be used with dictionaries too
def len_function():
    print(len(nums))        # 3
    
def add_nums():
    print(nums.get(1, "not found") +
          nums.get(2, "nf"))        # prints 'onetwo' bc it's adding the values of those keys: str("one") and str("two")
    
    