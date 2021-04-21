def first():
    c=0
    for i in range(1,11):
        c=c+i
    print(c)

def second():
    c=0
    for i in range(1,11):
        if i%2==0:
            c=c+i
        else:
            c=c-i
    print(c)

def third():
    c=0
    for i in range(1,11):
        if i%4==1:
            c=c+i
        elif i%4==2:
            c=c-i
        elif i%4==3:
            c=c-i
        elif i%4==0:
            c=c+i
    print(c)

def four(): 
    c=1 
    for i in range(1,10):
        for x in range(i+1,i+2):
            if i%2!=0:
                c=c-(i/x)
            else:
                c=c+(i/x)
    print(c)

def five():
    c=65
    b=0
    while c<=79:
        c=c+b
        print(chr(c),end="")
        b=b+1
    

def six():
    a=72
    for i in range(1,9):
        print(chr(a),end="")
        if i%2==0:
            a=a-i
        else:
            a=a+i
def seven():        
    c=65
    for i in range(0,4):
        c=c+i
    if i==0:
        print(chr(c))
    elif i==1:
        print(chr(c)+chr(c+2))
    elif i==3:
        print(chr(c)+chr(c+4)+chr(c+9))

space=2
for i in range(1,6,2):
   if i!=5:
       s=space-1
       p=s*" "
       print(p,i*"*")
   else:
       print(i*"*")
            

       
   

    
    



    
    

