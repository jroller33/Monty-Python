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


# print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']



def squares():
    start = int(input("Enter first number: "))
    end = int(input("Enter second number: "))


    result = [n*n for n in range(start, end+1)] 
    print(result)

squares()

# print(squares(2, 3)) # Should print [4, 9]
# print(squares(1, 5)) # Should print [1, 4, 9, 16, 25]
# print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def countries(countries_dict):
    result = ""
    for key,value in countries_dict.items():
        result += countries_dict[key]
        print(result)


# print(countries({"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia":["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))



    # countries = {
    #     "Africa": ["Kenya", "Egypt", "Nigeria"], 
    #     "Asia": ["China", "India", "Thailand"], 
    #     "South America": ["Ecuador", "Bolivia", "Brazil"]
    #     }


# host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
# print(host_addresses.keys())
