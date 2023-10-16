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


# s = 12
# p = 27
# for i in range(p):
#     number = 1
#     if i == 0:
#         continue
#     while number < s + p:
#         if number * i == p and number + i == s:
#             print(i, number)
#         number += 1

n = 1024
number = 1
print(number)
while number < n:
    number *= 2
    if number <= n:
        print(number)