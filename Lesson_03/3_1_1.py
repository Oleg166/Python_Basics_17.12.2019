#def my_pow(x):
#    return x ** 2

data = [-1, -2, -3, 1, 2, 3]

"""result = []
for i in data:
    result.append(my_pow(i))
print(result)

result = list(map(my_pow, data))
print(result)
def my_filter(x):
    return x > 0

result = list(filter(my_filter, data))
print(result)"""
result = list(map(lambda x: x ** 2, data))
print(result)
