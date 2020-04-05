'''
Reading and writing to the file. Modes for these operations:
r - Read only mode
w - write only mode
r+ - read and write mode
a - append mode
'''

# mode
# info to write

def writefile():
    list = [1000, 2000, 3000, 4444, 6666, "dfadsfsa", "fsdfsdf"]
    '''
    1000 is int or number
    '1000' is string
    
    '''

    file = open("test.txt", 'w')

    for i in list:
        print(i)
        file.write(str(i)+"\n")
    print("==========File Writing completed===========")
    file.close()

def readfile():
    file = open("test.txt", 'r')
    # print(str(file.read()))
    print(str(file.readline()))
    print(str(file.readline()))
    print(str(file.readline()))
    print("=========File reading completed==========")

writefile()
readfile()
