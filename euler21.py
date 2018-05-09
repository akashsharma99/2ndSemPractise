def get_sum(x):
    s=0
    for i in range(0,(x//2)+1):
        if(i==0):s=s+0
        elif(x%i==0):
            s=s+i
    return s
t = int(input())
for a0 in range(t):
    n = int(input())
    arr=[False]*(n+1)
    arr[0]=True
    s=0
    for index in range(n+1):
        if(arr[index]==False):
            s1=get_sum(index)
            #print(s1)
            arr[index]=True
            if(s1==index or s1<index):
                continue
            s2=get_sum(s1)
            if(s1<=n):arr[s1]=True
            if(s2==index):
                print(index)
                if(s1<n):
                    print(s1)
                    s=s+s1
                s=s+index
    print(s)
