
data_from_file = ['100(л)', '-', '20(лаб)']

result = 0
for i in data_from_file:
    if i.endswith('(л)') == True:
        result = result + int(i.replace('(л)', ''))
    elif i.endswith('(пр)') == True:
        result = result + int(i.replace('(пр)', ''))
    elif i.endswith('(лаб)') == True:
        result = result + int(i.replace('(лаб)', ''))
    else:
        result = result + 0
print(result)