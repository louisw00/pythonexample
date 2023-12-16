from collections import Counter

a = "aaaabbbccd"
mycounter = Counter(a)
print(mycounter)
print(mycounter.keys())  # return a dictionary
print(list(mycounter.items())[0])
print(mycounter.most_common(2))  # return a list
print(mycounter.most_common(1)[0][0])
