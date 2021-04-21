class Person:
    def __init__(self,name,weight,hp,ap):
        self.name =name
        self.weight=weight
        self.hp=hp
        self.ap=ap
    def eat(self,vol):
        self.weight=self.weight+vol
    def run(self):
        self.weight=self.weight-1
    def ua(self,tmp):
        
        self.hp=self.hp-tmp.ap
        ##自己本身的hp-別人的攻擊
    def a(self,tmp):
        tmp.hp=tmp.hp-self.ap
        ##(括號裡的人)-自身的攻擊

handsome=Person("黃天受",80,2000,100)
print(handsome)
print(handsome.name)
print(handsome.weight)

handsome.eat(4)
print(handsome.weight)
handsome.run()
handsome.run()
print(handsome.weight)

lee=Person("柯柯柯",80,1500,120)

lee.ua(handsome)
##lee被handsome攻擊
print(lee.hp)
lee.a(handsome)
##lee去攻擊handsome
print(handsome.hp)