list = [1, 2, 3, 4]
print(list)
print(*list)  # unpacking operator

# for this function, we need know the topping that everyone orders different with. we can use *arg. You can change to any name by adding asterisk in front of it.

# **kwarg means keywords arguments
# it will handle all the key arguments
# func2(**kwarg)=func2(arg2=2,arg1=3,arg3=4)


def order_pizza(size, *topping, **details):
    print(f'Ordered a {size} pizza with the following toppings:')
    for i in topping:
        print(f'-{i}')
    print("\nDetials of our orders are:")
    for key, value in details.items():
        print(f'-{key}:{value}')


order_pizza("large", "pepperoni", "pineapple", "olives", delivery=True, tip=5)
