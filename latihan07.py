list=[5,2,3,"luke",{"name":"John Doe"}]
list.append("Sepeda")
list.remove('luke')
print(list)

dict={}
dict={"Hero":"Batman","color":"black"}
print(dict)


class mobil():
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    def getSpeed(self):
        return self.max_speed
    def getMileage(self):
        return self.mileage

car=mobil(500,1000)
print(car.max_speed,car.mileage)

class parent:
    def __init__(self,Orangtua,Anak):
        self.Orangtua = Orangtua
        self.Anak = Anak

    def getOrangtua(self):
        return self.Orangtua
    def getAnak(self):
        return self.Anak
Nama=parent("Udin","Max")

print(Nama.Orangtua,Nama.Anak)

lst=[[31,4],[15,2],[51,8],[10,8],[35,11]]

def clubCatur(inpt):
    lsa=[]
    for i in inpt:
        if i [0] >30 and i[1] >= 5:
            lsa.append("Profesional")
        else:
            lsa.append("Open")
    return lsa
print(clubCatur(lst))