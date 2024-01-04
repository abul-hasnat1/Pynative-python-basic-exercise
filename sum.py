for i in range(0,10,1):
    if i==0:
        print ('current number: ',i, end=' ')
        print('previous number: 0',end=' ')
        print('sum: 0')

    else:
        print ('current number: ',i, end=' ')
        print('previous number: ',i-1,end=' ')
        print('sum: ',end=' ')
        print(i+i-1)