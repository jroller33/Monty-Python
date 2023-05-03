numbers1 = [4, 5, 2, 9, 6, 3, 7]
numbers1.sort() # modifies the original list
print(numbers1)

nums2 = [2, 5, 3, 7, 9, 6, 8]

print(sorted(nums2))    # sorted() doesn't modify the original list
print(nums2)


names = ["Dwight", "Angela", "Jim", "Pam"]
print(sorted(names)) # sorts alphabetically by default if it's a list of strings

print(sorted(names, key=len)) # sorts by the length of each string in the list