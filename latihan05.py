def root_number(x):
    z=0
    for y in str(x):
        z +=int(y)

    if z > 9:
        z = root_number(z)
    return z

print(root_number(1234))
class siswa:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    def getNama(self):
        return self.nama
obj = siswa('Luke','45')
print(obj.getNama())

def perpangakatan(x):
    y= ''
    for i in str(x):
        y +=str(int(i)**2)
    return int(y)
print(perpangakatan(248))