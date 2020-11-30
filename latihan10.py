x="Luke"
ls=["qwe",'123','fdd',"Luke"]
if 'Luke' in ls:
    print("exist")


lstBulan= ["Januari","Februari",'Maret',"april",'mei','juni','july','agustus','september','oktober','november','desember']
def bulan(x):
     return lstBulan[x -1]
print(bulan(1))

lstBulan= ["Januari","Februari",'Maret',"april",'mei','juni','july','agustus','september','oktober','november','desember']
class Bulan():
    def getNama(i):
        return lstBulan[i - 1]

myobjectx = Bulan()
print(Bulan.getNama(1))

class Bulan():
    lstBulan= ["Januari","Februari",'Maret',"april",'mei','juni','july','agustus','september','oktober','november','desember']
    def getNama(i):
        return lstBulan[i - 1]

myobjectx = Bulan()
print(Bulan.getNama(2))


class Bulan:
    lstBulan = ["Januari","Februari",'Maret',"april",'mei','juni','july','agustus','september','oktober','november','desember']
    
    def __init__(self,index,second):
        self.index = index
        self.second = second
    def getNama(self):
        antara = ", ".join(self.lstBulan[self.index:self.second - 1])
        satu = self.lstBulan[self.index - 1]
        dua = self.lstBulan[self.second -1]
        if len(antara) > 0:
            return "Di antara Bulan " +  satu  + " dan " + dua + " adalah bulan " + antara
        return " Tidak ada bulan di antara " + satu +" dan " + dua

bulan = Bulan(1,2)
print(bulan.getNama())


class qwe:
    lstBulan = ["Januari","Februari",'Maret',"april",'mei','juni','july','agustus','september','oktober','november','desember']
    
    def __init__(self,index):
        self.index = index
    
    def getName(self):
        return self.lstBulan[self.index - 1]

bln = qwe(2)
print(bln.getName())