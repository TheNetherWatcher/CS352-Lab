# 1. Basic Operations with Numbers
def basic_operations():
    x = 10  # integer
    y = 5.5  # float
    
    # Sum, Difference, Product, Quotient
    print("Sum:", x + y)
    print("Difference:", x - y)
    print("Product:", x * y)
    print("Quotient:", x / y)
    
    # Shorthand operator
    x += 5
    print("Updated x (after += 5):", x)

# 2. String Manipulation
def format_string(name, age):
    formatted1 = "My name is {} and I am {} years old.".format(name, age)
    formatted2 = f"My name is {name} and I am {age} years old."
    return formatted1, formatted2

# 3. List Operations
def list_operations():
    numbers = list(range(1, 11))
    
    # Squares using list comprehension
    squares = [n ** 2 for n in numbers]
    print("Squares:", squares)
    
    # Extract even numbers
    evens = numbers[1::2]  # Even numbers using slicing
    print("Even numbers:", evens)

# 4. Dictionary Manipulation
def dictionary_operations():
    students = {"Alice": 85, "Bob": 90, "Charlie": 78}

    # Add a new student
    students["David"] = 92

    # Retrieve marks
    print("Marks of Bob:", students.get("Bob"))

    # Print sorted dictionary
    for name in sorted(students):
        print(f"{name}: {students[name]}")

# 5. Set Operations
def set_operations():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}

    # Union, Intersection, Difference
    print("Union:", set1 | set2)
    print("Intersection:", set1 & set2)
    print("Difference:", set1 - set2)

    # Unique elements
    unique_elements = list(set1 ^ set2)
    print("Unique elements:", unique_elements)

# 6. Tuples and Functions
def tuple_operations(t):
    if not t:
        return None, None, 0
    return max(t), min(t), sum(t)

# Sample function calls
print("Basic Operations:")
basic_operations()
print("\nString Manipulation:")
print(format_string("John", 25))
print("\nList Operations:")
list_operations()
print("\nDictionary Manipulation:")
dictionary_operations()
print("\nSet Operations:")
set_operations()
print("\nTuple Operations:")
print(tuple_operations((10, 20, 30, 40)))