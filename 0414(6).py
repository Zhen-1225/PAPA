class Wheel:
    def __init__(self,size):
        self.size=size
class Engine:
    def __init__(self,cc):
        self.cc=cc
class Car:
    def __init__(self):
        self.eg=None
        self.fr=None
        self.fl=None
        self.br=None
        self.bl=None

person=Car()
person.eg=Engine(2000)
person.fr=Wheel(1)
person.f1=Wheel(2)
person.br=Wheel(3)
person.bl=Wheel(4)
print(person.fr.size)


