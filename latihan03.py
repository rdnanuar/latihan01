a= 10
b= 7
hasil=a + b
print(a,'+',b,'=',hasil)

hasil=a - b
print(a,'-',b,'=',hasil)

hasil=a * b
print(a,'*',b,'=',hasil)

hasil=a / b
print(a,'/',b,'=',hasil)

hasil=a ** b
print(a,'**',b,'=',hasil) # Pangkat eksponen

hasil=a % b
print(a,'%',b,'=',hasil) # sisa pembagaian modulus

hasil=a // b
print(a,'//',b,'=',hasil)# dibulatkan kebawah floor divison

x= 3
y= 2
z= 4

hasil= x ** y * z + x / y - y % z //x
print(hasil)

hasil= x ** y * (z + x) / y - y % z //x
print(hasil)

hasil= x + y * z
print(hasil)


hasil= (x + y) * z
print(hasil)

# count = (3,6,9,12,15)
# while count < 20 :
#     print(count)
#     count +=1

index = 3
while index < 20:
    print(index)
    index +=3
index = 3
while index < 20:
    if index %3 ==0:
        print(index)
    index +=1
print("====Break====")
count =0
while True:
    print(count)
    count +=1
    if count >= 5:
        break
print ("=====Continue=====")
for x in range(10):
    if x %2 == 0:
        continue
    print(x)
print("====Statment Else in Looping")
for i in range (1,10):
    if(i%5==0):
        break
    print(i)
else:
    ("salah")
print("Ganjil")


for x in range(10):#ganjil
    if x %2 ==0:
        continue
    print(x)

print("Genap")
for y in range(1, 11):
    if y%2 == 0:
        print(y)
    y +=1

def jumlah(a,b):
    c = a + b
    return c
hasil=jumlah(4,5)
print(hasil)

def bilangan(start, end):
    while start < end:
        if start %3 ==0:
            print(start)
        start +=1
bilangan(1,30)


def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

def modulus(a, b):
    return a % b

def perpangkatan(a, b):
    return a ** b

print('+')
print('-')
print('*')
print('/')
print('%')
print('**')
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
elif pilih == "%":
    print(A,'%',B,'=',modulus(A,B))
elif pilih == "**":
    print(A,'**',B,'=',perpangkatan(A,B))

else :
    print("salah memasukan Operasi")
