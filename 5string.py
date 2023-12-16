# ordered,immutable
mystring = "Hello World"
print(mystring[0])
# mystring[0] = "h" this is 🙅 coz its immutable


# method of string
my_list = mystring.split(" ")
print(my_list)

# the best way to list -> string  dont use loop
newstring = " ".join(my_list)
print(newstring)
