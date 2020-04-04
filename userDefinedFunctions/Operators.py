def operations(a, b):
    return (a ** b)

# print(operations(2, 5))


def compare(a, b):
    if (a<b):
        print (str(a)+" a is smaller")
    if (b<a):
        print (str(b)+ " b is smaller")

# compare(20,4)


def checkPresent(i):
    if i not in ('a', 'b', 'c'):
        print (i + " Not Present")
    else:
        print(i + " Present")

# checkPresent("x")

def checkEqual(i):
    if i is not "A":
        print("is NOT A")
    else:
        print ("is A")
checkEqual("a")
