# Example 1 - try and except block
def divide(num1, num2):
    try:
        try:
            print("new another try block inside finally block")
        except:
            print("new another except block inside finally block")
        finally:
            print("new another finally block inside first finally block")

        # print(a)
        # return int(num1)/int(num2)
        result = int(num1)/int(num2)
        return result
    except TypeError:
        print("Expected int value but observed str value")
    except ZeroDivisionError:
        print("The second number is Zero. Please provide non zero value.")
    except NameError:
        print("Undefined variable used")
    finally:
        try:
            print("another try block inside finally block")
        except:
            print("another except block inside finally block")
        finally:
            print("another finally block inside first finally block")

        print("End of the Function")

    # except Exception:
    #     print("An invalid data is provided")


num1 = input("Enter first number:\n")
num2 = input("Enter second number:\n")

print(divide(num1, num2))

