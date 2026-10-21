# Example 1: Numbers
age = 2
height = 1.75
print("Age:", age)
print("Height:", height)

# Example 2: Strings
name = "Sri Sarvesh"
print("Name:", name)

# Example 3: Booleans
is_student = True
print("Is student:", is_student)

# Example 4: Check data types
print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

# Example 5: Type conversion
number = "100"
converted_number = int(number)
print(converted_number + 50)

# Example 6: User input
user_name = input("Enter your name: ")
print("Welcome,", user_name)

# Example 7: F-strings
name = " Sri Sarvesh"
course = "Computer Science and Engineering"
clg = "Dr.NGP Institute of Technology"
print(f"{name} studies {course} at {clg}.")

# Example 8: String methods
text = "full stack developer"
print(text.upper())
print(text.lower())
print(text.strip())

# Example 9: Temperature converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")

# Example 10: checks if a number is even or odd
num = int(input("Enter a number: "))
print(num % 2 == 0)