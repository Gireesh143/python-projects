def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if(y==0):
        return "Cannot divide by zero!"
    return x/y

def main():
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter the choice(1/2/3/4): ")

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if choice == '1':
        print("Result:", add(num1,num2))
    elif choice == '2':
        print("Result:", subtract(num1,num2))
    elif choice == '3':
        print("Result:", multiply(num1,num2))
    elif choice == '4':
        print("Result:", divide(num1,num2))
    else:
        print("Invalid input")


while True:
    main()
