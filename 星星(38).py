star=int(input("輸入"))
a=(star//2)-1
b=0

for i in range(1,star+1,2):
    if i!=star:        
        ya=a*" "               
        print(ya,i*"*")
        a=a-1
    else:
        print(i*"*")
for i in range(star-2,-1,-2):
    if i==i:
        ha=b*" "
        print(ha,i*"*")
        b=b+1
