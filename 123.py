Apple=input("請輸入一個數").split(",")
BB=sorted(Apple)
CC=sorted(Apple,reverse=True)
print(CC)
AA=len(Apple)
max=""
min=""
for i in range (AA):
    W=BB[i]
    X=CC[i]
    max+=W
    min+=X
print(int(max)-int(min))


