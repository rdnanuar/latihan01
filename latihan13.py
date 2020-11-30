class Parent(object):

    def getParentName(self):
        return 'parent'

class Child(Parent):

    def getName(self):
        return "Child"

chld = Child()

print(chld.getParentName())
print(chld.getName())



class Minuman():

    def getAirMineral(self):
        return 'AQUA'
    
class Air(Minuman):

    def getNama(self):
        return "Ades"

class Makanan(Air,Minuman):

    def getNamee(self):
        return "Cireng"
    
qwe = Makanan()

print(qwe.getAirMineral())
print(qwe.getNama())
print(qwe.getNamee())