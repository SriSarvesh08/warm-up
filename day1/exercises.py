# Exercise 1: FizzBuzz
def fizzbuzz(limit=20):
    for number in range(1, limit + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

# Exercise 2: Prime number check
def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

# Exercise 3: Palindrome check
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

# Exercise 4: Factorial
def factorial(number):
    if number < 0:
        return "Factorial is undefined for negatives"
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result


# Exercise 5: Sum using *args
def calculate_sum(*args):
    total = 0
    for number in args:
        total += number
    return total

# Exercise 6: Greeting with a default argument
def greet(name="Student"):
    return f"Hello, {name}!"

# Exercise 7: Find even numbers using continue and break
def print_even_numbers(limit=20):
    for number in range(1, limit + 1):
        if number > 15:
            break
        if number % 2 != 0:
            continue
        print(number)

# Exercise 8: Display details using **kwargs
def display_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
if __name__ == "__main__":
    print("1. FizzBuzz")
    fizzbuzz(15)

    print("\n2. Prime check")
    print(is_prime(17))

    print("\n3. Palindrome check")
    print(is_palindrome("madam"))

    print("\n4. Factorial")
    print(factorial(5))

    print("\n5. Sum using *args")
    print(calculate_sum(10, 20, 30))

    print("\n6. Default argument")
    print(greet())
    print(greet("Sarvesh"))

    print("\n7. Even numbers")
    print_even_numbers(20)

    print("\n8. Keyword arguments")
    display_details(name="Sarvesh", course="Python", level=1)
