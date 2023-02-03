# list comprehensions are used to quickly create lists that obey a rule
# they're like set-builder notation in math

def cubes():
    cubes = [i**3 for i in range(5)]
    print(cubes)    #   [0, 1, 8, 27, 64]
    
def evens():
    evens = [i**2 for i in range(10) if ( i**2 % 2 == 0 )]
    print(evens)    #   [0, 4, 16, 36, 64]
    
def consonants_only():
    word = input("Enter a word: ")
    vowels = { 'a', 'e', 'i', 'o', 'u' }
    consonants = [for i in word if i not in vowels]
    print(consonants)