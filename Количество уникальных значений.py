
numbers = list(map(int, input().split()))
new_list = []
for x in numbers:
    if x  not in new_list:
        new_list.append(x)

s = len(new_list)
print(s)