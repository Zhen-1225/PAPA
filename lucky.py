
boy=input("算一下:").split()
girl=input("算兩下").split()
i=0
BB=0
DD=0
EE=0
FF=0
for i in range(8):
    AA=int(boy[i])
    BB=BB+AA
    CC=int(girl[i])
    DD=DD+CC
if BB<10 and DD<10:
    print(str(BB+DD))
elif DD<10:
    while BB>=10:        
        for i in str(DD):
            FF=FF+int(i)
        if DD<10:
            break
        print(str(DD)+str(FF))
elif BB<10:
    while DD>=10:
        for i in str(BB):
            EE=EE+int(i)
        if EE<10:
            break
        print(str(BB)+str(EE))
elif BB>=10 and DD>=10:
    while BB>=10:
        for i in str(BB):
            EE=EE+int(i)
        if EE<10:
            break
    while DD>=10:                            
        for i in str(DD):
            FF=FF+int(i)
        if FF<10 :
            break
    print(str(EE)+str(FF))
       









