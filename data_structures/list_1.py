name="tecanvass"
year=2020

# list iteration
list = ['a', 'b', 'c', 'd', 1, 2, 3, 1.1, 2.2]
print(list)

# for a in name:
#     print(a)

# print(list[-5])

print(list[-5:-2])
print(list[2:5])

list[-5:-2] = [11,22,33]
print(list)

# list[3] = 'dd'
# print(list)

list1 = [0,1,2,3,4,5,[11,22,('a', 'b', 'c'),44],1.1, 2.2, 3.3]
print(list1[6][2][1])