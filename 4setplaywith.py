# Set - curly braacket
# 0 create
myset = {0, 1, 2, 3, 4, 5}
oddset = {1, 3, 5}
evenset = {0, 2, 4}
yourset = {0, 2, 100}
# 1 add
myset.add(4)  # no duplicate
print(myset)


# union & intersection
u = oddset.union(evenset)
print(u)
i = oddset.intersection(evenset)
print(i)

# differecne
diff = myset.difference(yourset)
print(diff)
sdiff = yourset.symmetric_difference(myset)
print(sdiff)  # 所有的difference

# 改变原来set 不需要建立new set
print(myset)
myset.difference_update(yourset)
print(myset)
myset.update(yourset)
print(myset)
