# lambda argument : expression

#### sort###
from functools import reduce
points20 = [(1, 2), (15, 1), (5, -1), (10, 4)]
points20_sorted = sorted(points20)
points20_sorted_y = sorted(points20, key=lambda x: x[1])

points20_sorted_sum = sorted(points20, key=lambda x: x[1]+x[0])


print(points20)
print(points20_sorted)  # sorted by x
print(points20_sorted_y)  # sorted by y
print(points20_sorted_sum)  # sorted by y

### map(function(x),list)###
mylist = [1, 2, 3, 4, 5]
mylist_mapped = map(lambda x: x*x, mylist)
mylist_listed = [x*x for x in mylist]
print(list(mylist_mapped))
print(mylist_listed)


###  filter(true,list) ######
yourlist = [1, 2, 3, 4, 5, 6, 7]
yourlist_filtered = filter(lambda x: x > 4, yourlist)
print(list(yourlist_filtered))
yourlist_list = [x for x in yourlist if x > 4]
print(yourlist_list)

####### reduce(function(x,y),sequence)###
yourlist_reduced = reduce(lambda x, y: x*y, yourlist)
print(yourlist_reduced)
