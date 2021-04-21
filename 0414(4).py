class Head:
    def __init__(self,size):
        self.size=size

class Body:
    def __init__(self,volume):
        self.volume=volume
class Hand:
    def __init__(self,lenth):
        self.lenth=lenth
class leg:
    def __init__(self,width):
        self.width=width
class Person:
    def __init__(self,head,body,rh,lh,rl,ll):
        self.head=head
        self.body=Body
        self.rh=rh
        self.lh=lh
        self.rl=rl
        self.ll=ll
        ##6個屬性
lee=Person(Head(10),Body(2000),Hand(20),Hand(22),leg(30),leg(30))
print(lee.head.size)

