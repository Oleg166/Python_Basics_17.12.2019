"""my_list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_list_2 = [[10, 10, 10], [10, 10, 10], [10, 10, 10]]

# my_list_1 = [[1, 2], [3, 4]]
# my_list_2 = [[5, 6], [7, 8]]

for i in my_list_1:
    for j in i:
        print(j, end=" ")
    print()
print("+")

for i in my_list_2:
    for j in i:
        print(j, end=" ")
    print()

my_list_3 = []

for i in range(0, len(my_list_1)):
    my_list_4 = []
    for j in range(0, len(my_list_1[0])):
        my_list_4.append(my_list_1[i][j] + my_list_2[i][j])
    my_list_3.append(my_list_4)
print("=")

for i in my_list_3:
    for j in i:
        print(j, end=" ")
    print()
"""
a = 0
b = 5

for i in range(0, a//b):
    print("*" * b, end=r'\n')
if a//b != 0:
    print("*" * (a % b))
elif a == 0:
    print("Ничего не осталось")
elif a < b:
    print("*"*a)
