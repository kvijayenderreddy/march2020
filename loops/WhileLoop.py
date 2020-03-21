# i = 1
# while i<10:
#     print("value of i: ", i)
#     i=i+1

# Assignment 1
list2 = [1,2,3,4,5,6,7,8,9,10,11,12,15,18,20,24,25,27,30,32,33]
# count items divisible by 2,3,4,5,7:
# list the items as well
# items divisible by 2: []
# items divisible by 3: []
# items divisible by 4: []
div2 = 0
div3 = 0
div5 = 0
for a in list2:
    if a%2 == 0:
        div2 = div2+1
    if a%3 == 0:
        div3 = div3+1
    if a%5 == 0:
        div5 = div5+1

print("div by 2:",div2)
print("div by 3:",div3)
print("div by 5:",div5)

