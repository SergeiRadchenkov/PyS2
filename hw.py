# coins = [1, 1, 1, 1, 0]
# zero = 0
# one = 0
# for i in range(len(coins)):
#     if coins[i] == 0:
#         zero += 1
#     else:
#         one += 1
# if zero < one:
#     print(zero)
# else:
#     print(one)


s = 12
p = 27
number = 1
for i in range(p):
    number = 1
    if i == 0:
        continue
    if number * i == p:
        elif number + i == s:
        number += 1
        if number == p:
            break
    print(i, number)
    print(number, i)