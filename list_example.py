
# list_example.py
# Basic Python List Example

# 1. Create a List
fruits = ["Apple", "Banana", "Orange", "Mango"]

print("=== Python List Example ===")
print("Original List:", fruits)

# 2. Access List elements
print("\n=== Access Elements ===")
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])

# 3. Add an element
print("\n=== Add Element ===")
fruits.append("Grape")
print("After append:", fruits)

# 4. Insert an element
fruits.insert(1, "Watermelon")
print("After insert:", fruits)

# 5. Update an element
print("\n=== Update Element ===")
fruits[0] = "Strawberry"
print("After update:", fruits)

# 6. Remove an element
print("\n=== Remove Element ===")
fruits.remove("Banana")
print("After remove:", fruits)

# 7. List length
print("\n=== List Length ===")
print("Total fruits:", len(fruits))

# 8. Loop through List
print("\n=== For Loop ===")
for fruit in fruits:
    print(fruit)

# 9. Sort List
print("\n=== Sort List ===")
fruits.sort()
print("Sorted List:", fruits)

# 10. Reverse List
print("\n=== Reverse List ===")
fruits.reverse()
print("Reversed List:", fruits)

print("\n=== Program Finished ===")
