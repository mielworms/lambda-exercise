age = [('Mom', 45), ('Dad', 55), ('Son', 18), ('Daughter', 20)]
print("Original list:")
print(age)
age.sort(key = lambda x: x[1])
print("\nList sorted: ")
print(age)
