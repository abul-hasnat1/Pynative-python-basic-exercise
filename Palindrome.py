# Exercise 9: Check Palindrome Number
num=12322
num=str(num)
Flag= True
count=len(num)-1

for i in range(0,len(num)):
    if num[i]==num[count]:
        Flag=True
    else:
        Flag=False
    count-=1

if Flag==True:
    print('Palindrome')
else:
    print('Not Palindrome')