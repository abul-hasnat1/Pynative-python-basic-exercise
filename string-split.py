str="Emma is a good developer"



lst=str.split(" ")

print (lst)
count=0
for i in lst:
    if "a"==i:
        count+=1
print(count)
