n=input("幾次小考、幾位學生").split()
m=int(n[0])
w=int(n[1])

Arr=[list(range(m))for i in range(w)]
king=[]
popo=(input("幾%:").split())
for i in range(w):
    A=input("成績:").split()
    for j in range(m):
        Arr[i][j]=A[j]
        king.append(int(Arr[i][j]))

c=0 
grade=0  ##要宣告一次， ex:grade=grade+1
for k in range(m*w):
    if c==m:
        c=0    
    elif k==m*w:
        break
    grade=grade+(float(popo[c])*king[k])
    c=c+1
print(grade)
print(round((grade/w),2))