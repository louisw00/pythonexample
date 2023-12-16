from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import groupby
from itertools import chain
a = [1, 3]
b = [4, 5]
c = product(a, b)
print(list(c))


d = [1, 2, 3, 4]
perm = permutations(d, 2)
comb = combinations(d, 2)
print(list(perm))
print(list(comb))

persons = [{"name": "Louis", "age": 28}, {"name": "jimmy", "age": 27}, {"name": "Ada", "age": 28},
           {"name": "Kim", "age": 20}]

# groupby 必须针对sorted list
persons.sort(key=lambda x: x['age'])
grouped_by_age = groupby(persons, key=lambda x: x['age'])
for key, value in grouped_by_age:
    print(key, list(value))


# 合并两个lists
# print(list(chain(a, b)))
for i in chain(a, b):  # 不产生新的list
    print(i)
