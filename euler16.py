li=[]
str=pow(2,1000)
s=0
while(str!=0):
    s=s+(str%10)
    str=str//10
print(s)
