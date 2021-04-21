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
    def __init__(self):
        self.head=None
        self.body=None
        self.rh=None
        self.lh=None
        self.rl=None
        self.ll=None
        ##6個屬性
lee=Person()
lee.head=Head(20)
lee.body=Body(2000)
lee.rh=Hand(20)
lee.rl=Hand(22)
lee.rl=leg(30)
leg.rl=leg(30)
print(lee.head.size)

