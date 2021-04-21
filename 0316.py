li=[87,80,3,33,90,100,99,88,66]
for i in range(0,len(li)-1):
    if li[i]>li[i+1]:
        tmp=li[i]
        li[i]=li[i+1]
        li[i+1]=tmp  
    else:
        tmp=li[i+1]
        li[i+1]=li[i]
        li[i]=tmp 

print(li)
for x in range(0,len(li)-1):
    if li[x]>li[x+1]:
        tmp=li[i]
        li[x]=li[x+1]
        li[x+1]=tmp 
print(li)       
        