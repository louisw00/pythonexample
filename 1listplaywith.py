# list
# 0. Create list by SQUARE bracket
#    Create tuple by PARANTHESE
#    Create dictionary by curly
# bracket/braces
#    Create set by curly bracket
mylist1 = [1, "hello", True]
mylist2 = list()
mylist3 = [5]*5
fruitlist = ["apple", "banana", "pear", "cherry"]
print(mylist3)
# 1. list has index
print(mylist1[0])
print(mylist1[1])
print(mylist1[2])
# 2. iterate the list
for index, i in enumerate(fruitlist):
    print(index, i)
# 3.check the item in list
print("banana" in fruitlist)
# 4.add items in list
fruitlist.append("orange")
fruitlist.insert(0, "dragonfruit")
fruitlist.pop()
fruitlist.remove("apple")

print(fruitlist)
# 5.sort/reverse list
# 6.slice list
print(fruitlist[1:4])  # the last one is not included
# 7. copy list dont use =
fruitlist2 = fruitlist[:]  # method 1
fruitlist3 = fruitlist.copy()  # method 2
fruitlist4 = list(fruitlist)  # method 2
print(fruitlist2)
print(fruitlist3)
print(fruitlist4)
# 8.calculate in list
print([i*i for i in mylist3])

# 9.comprehensions
x = [0 for j in range(100) if j % 2 == 0]
print(x)

y = [[0 for _ in range(5)] for _ in range(5)]
print(y)

# 10.zip function
name = ["louis", "tim"]
age = [20, 30]
print(list(zip(name, age)))
