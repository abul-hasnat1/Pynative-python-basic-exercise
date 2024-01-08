# Exercise 12: Calculate income tax for the given income by adhering to the rules below

num= 45000

tax=0

if num<10000:
    print("tax; ", tax)

else:
    if num<20000:
        tax=tax+(num-10000)*0.1
    else:
        tax=1000 + (num-20000)*0.2

print(tax)
