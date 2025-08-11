
list_numbers = list(map(int, input().split()))

list_unique_numbers = []

for number in list_numbers :
    if number not in list_unique_numbers :
       list_unique_numbers.append(number)

print(len(list_unique_numbers))

