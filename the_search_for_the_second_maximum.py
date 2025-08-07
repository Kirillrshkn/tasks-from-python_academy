# version 1
#
# n = int(input())
# scores = list(map(int, input().split()))
# max_score = max(scores)
# new_list = []
#
#
# for i in scores:
#     if len(scores) > n or len(scores) < n:
#         raise TypeError('Длинна строки должна быть ровна n')
#
#     elif i < max_score:
#         new_list.append(i)
#
# print(scores)
# print(max_score)
#
# if new_list:
#     r = max(new_list)
#     print(r)

# version 2

# n = int(input())
# scores = list(map(int, input().split()))
# len_scores = len(scores)
#
# if len_scores > n < len_scores :
#     print('Длинна списка должна быть ровна n')
#
# else:
#     scores.sort(reverse=True)
#     max1 = scores[0]
#     max2 = scores[1]
#
# print(max2)

# version 3

n = int(input())
scores = list(map(int, input().split()))

max1 = max2 = float('-inf')

len_scores = len(scores)

if len_scores > n < len_scores :
    raise TypeError('Длинна списка должна быть ровна n')

for i in scores :
    if  i > max1:
        max2 = max1
        max1 = i

    elif n > max2 and n != max1:
        max2 = n

print(max2)