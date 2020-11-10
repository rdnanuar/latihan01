listname=["Baju","Celana","Sepatu"]
print(listname[0:2])
print(listname[::-1])

# for variable in listname:
#     print(variable)

number = 1 + 2 + 3 / 4,0
print(number)

mod = 10 % 3
print(mod)

helloworld= "hello "+ "" + "world"
print(helloworld)


print("=======Using method lists=====")
even_numbers = [2,4,6,8]
ood_numbers = [1,3,5,7]

all_numbers= even_numbers + ood_numbers
print(all_numbers)

print("====String Formating=====")
myString = "Luke Skywalker"

myInt=12
myFloat=4.8

print(f"my string is %s" % myString)
print(f"This is integer number %d" % myInt)
print(f"The string %s and the integer %d" %(myString,myInt))

# string format

print("the string format {} and the integer {}".format(myString,myInt))

print(f"====refrence use index=====")
print(f"The string is {0} and integer is {1}".format(myString,myInt))


astring = "Hello world !"
print(astring.index("o"))

astring = "Hello world!"
print(astring[3:7:2])

astring = "Hello world!"
print(astring[::-1])
print(astring.upper())
print(astring.lower())

astring= "Hello world !"
print(astring.startswith("hello"))
print(astring.endswith("hasdasdasdasdasd"))

aspring = "Hello Wolrd !"
afewwords =astring.split(" ")
print(afewwords)

x = 2
print(x == 2)
print(x == 3)
print(x < 3)

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is john, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John Or Rick.")



nilai=49
if 80 <= nilai <=100:
    print("Nilai anda adalah A")
elif 70 <= nilai <80:
    print("Nilai anda adalah B")
elif 60 <= nilai <70:
    print("Nilai anda adalah C")
elif 50 <= nilai <60:
    print("Nilai anda adalah D")
else :
    print("Anda Tidak Lulus")


x= 12
y= 12
print('nilai x =,',x,',id =',hex(id(x)))
print('nilai y =,',y,',id =',hex(id(y)))
hasil= x is y
print('x is y =',hasil)

x= "3"
y= 3
hasil = x is y
print(hasil)

