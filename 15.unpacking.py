a, b = (1, 2)
print(a)  # 如果只print a 那么b就浪费了

c, _ = (1, 2)
print(c)


a, b, *_, d = (1, 2, 3, 4, 5, 6)
print(a)
print(b)
print(d)
