# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

num= 54321
num=str(num)

for i in range(len(num)-1,-1,-1):
    print(num[i], end=' ')