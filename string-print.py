# Write a program to accept a string from the user and display characters that are present at an even index number.
# Exercise 3: Print characters from a string that are present at an even index number
user=input("Enter: ")
for i in range(len(user)):
    if i%2==0:
        print(user[i])