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

# ITERATING OVER A LIST AND TUPLE

def iterate_list():
    # for each string in the list, get its length and add it to the total
    # len() is used to get length of string and number of elements in the list
    animals = ["Dog", "Cat", "Bird", "Fish", "Snake"]
    x = 0
    for animal in animals:
        x += len(animal) # length of each string in the list
        
    # len(animals) is used to get the number of elements in the list
    print(f"Total characters: {x}, Average length: {x / len(animals)}")
    
def enumerate_function():
    # enumerate() takes a list as a parameter and returns a tuple for each element in the list. The first value in the tuple is the index, and the second is the element from the list at that index.
    
    winners = ["Ashley", "Dylan", "Reese"]
    for index, person in enumerate(winners):
        print(f"{index + 1} -- {person}")
        
def full_emails(people):
    result = []
    for email, name in people:
        result.append(f"{name} <{email}>")
    return result

# print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com")]))

# list comprehensions:

def list_comprehensions():
    multiples = []
    for x in range(1, 11):
        multiples.append(x*7)
    print(multiples)
    
    # or you could do it this way:
    multiples2 = [x*7 for x in range(1, 11)]
    print(multiples2)
    
    # list comprehensions create new lists based on ranges or sequences
    languages = ["HTML", "JavaScript", "Python", "Ruby"]
    lengths = [len(language) for language in languages]
    print("Lengths of strings in array: ", lengths)
    
    # list comps can use a conditional stmt to filter out values
    divisible_by_3 = [x for x in range(0, 101) if x % 3 == 0]
    print(divisible_by_3)
    
    # create a fn, takes 'n' as arg, returns a list of odd #s btw 1 and n inclusively
def odd_nums(n):
    return [ x for x in range(1, n + 1) if x % 2 != 0 ]
    
    # the odd_nums(n) function does the same thing as this long code:
    # my_list = []
    # for x in range(1,101):
    # if x % 10 == 0:
    #     my_list.append(x)
    # print(my_list)

def replace_file_extensions():
    # this uses a list comprehension to replace all ".hpp" extensions with ".h"
    filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

    newfilenames = [filename.replace(".hpp", ".h") if filename[-4:] == ".hpp" else filename for filename in filenames]

    print(newfilenames)

def pig_latin():
    text = input("Enter a phrase: ")
    words = text.split()
    pig_latin = ""

    for word in words:
        word = word[1:] + word[0] + "ay "
        pig_latin += word
    
    print(pig_latin)


def convert_linux_permissions():
    octal = input("Please enter an octal (Ex: 640): ")
    
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += "-"

    print(f"Linux file permissions: {result}")

def group_list(group, users):
    return group + ": " + ", ".join(users)

# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # "Marketing: Mike, Karen, Jake, Tasha"

def guest_list(guests):    
    # unpacks each tuple
	for guest in guests:
		(name, age, job) = guest
		print(f"{name} is {age} years old and works as {job}")

# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

