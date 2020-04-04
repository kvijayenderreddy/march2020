# list = [1,2,3,4,5]

def myName(name="Rayesa"):
    print("My Name is", name)
    # print("My Name is " + name)
# myName(list)

def listItertion(list):
    for i in list:
        print(i)
# listItertion(list)

def myNewName(name='Anjali'):
    returnString = "My Name is" + name
    print(returnString)
    return returnString
# print(myNewName("Preeti"))

def ourNames(name1, name2, name3):
    print("Class attendees:\n", name1, name2, name3)
# ourNames("Anjali", "Preeti", "Rayesa")
# ourNames(name2="Preeti", name1="Anjali", name3="Rayesa")


# Create a function which takes one parameter and will return the parameter value 3 times

def iterate3Times(text):
    for i in range (3):
        print (text)

# iterate3Times("Rayesa")



def my_func(value1, iterations):
    print((value1+"\n") * iterations)
    # for i in range(3):
    #     print (value1)

my_func("Test", 4)

# Create the function taking two parameters with first the string, and other the integer iteration count


# def value(name='ray'):
#     for i in list:
#         return("hello", name)
#
#
# print(value(1))
# print(value(2))
# print(value(3))


