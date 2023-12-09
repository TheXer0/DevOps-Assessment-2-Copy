# A simple program to calculate sum of two numbers


def calculate_sum(a, b):
    return a + b

def check_even_odd(sum):
    if sum % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    try:
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
        Sum = calculate_sum(a, b)
        print("Sum of the two numbers:", Sum)
        print("The sum is an", check_even_odd(Sum), "number.")
    except ValueError:
        print("Please enter a valid integer.")




