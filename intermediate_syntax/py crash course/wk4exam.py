def format_address():

    address_string = input("Please enter an address: ")
    
    house_number = ""
    street_name = ""

    address_parts = address_string.split()

    for address_part in address_parts:
        if address_part == address_parts[0]:
            house_number = address_part
        else:
            street_name += address_part + " "

    print(f"House number {house_number} on a street named {street_name.strip()}")
    

def string_words(string):
    # Complete the return statement using both a string operation and 
    # a string method in a single line.
    return len(string.split())


# print(string_words("Hello, World")) # Should print 2
# print(string_words("Python is awesome")) # Should print 3
# print(string_words("Keep going")) # Should print 2
# print(string_words("Have a nice day")) # Should print 4


def alphabetize_lists(list1, list2):

    list = list1 + list2
    new_list = sorted(list)

    return new_list 


Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]


print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']

