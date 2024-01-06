def list_check(l):
    a=len(l)-1
    if l[0]==l[a]:
        return True
    else:
        return False
    
print(list_check([10, 20, 30, 40, 10]))
print (list_check([75, 65, 35, 75, 30]))
