print("SIMPLE CALCULATOR")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nResults:")
print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)

if b != 0:
    print("Division       :", a / b)
    print("Modulus        :", a % b)
else:
    print("Division       : Cannot divide by zero")
    print("Modulus        : Cannot calculate modulus by zero")