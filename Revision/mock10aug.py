try:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))

    result = a/b
    print("Result: ",result)
except ValueError:
    print("Please enter numbers only")
except ZeroDivisionError:
    print("We Cannot divide by zero")
except Exception:
    print("Other Error occured")
finally:
    print("Division is succeed")

