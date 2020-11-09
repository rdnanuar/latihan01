list=[1, 2 ,3, 4, 5, 6, 7]

for x in list:
    print(x)


def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

print('+')
print('-')
print('*')
print('/')
pilih=input("Masukan Nilai Operasi:")
A=int(input("Angka Pertama :"))
B=int(input("Angka Kedua :"))
if pilih == "+":
    print(A,"+",B,'=',tambah(A,B))
elif pilih == "-":
    print(A,"-",B,'=',kurang(A,B))
elif pilih == "*":
    print(A,'*',B,'=',kali(A,B))
elif pilih == "/":
    print(A,'/',B,'=',bagi(A,B))

else :
    print("salah memasukan Operasi")
    
