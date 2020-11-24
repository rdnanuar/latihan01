def persegi(p , l):
    return p * l
def Pangkat(n):
    return n**2
def LuasSegitiga(i,q):
    return 0.5 * i * q

print(persegi(8,2))
print(Pangkat(8))
print(LuasSegitiga(8,2))


_inpt = [1,5,6,2,8]

def bebas(ipt_):
    x = []
    for i in ipt_:
        x.append(i ** 2)
    return sum(x)
print(bebas(_inpt))

def qwe(numbers):
    return sum(i**2 for i in numbers)
print(qwe(_inpt))

_dict = {}

_dict["john"] = "09809809012832"
_dict["peter"] = "09809809012831"
_dict["qwe"] = "09809809012833"
for d,v in _dict.items():
    print(f"{d} the phone is {v}")

user = [
    {
        "username": " luke", 
        "email" : "luke@gmail.com"
    },

    {
        "username": " qwe", 
        "email" : "qwe@gmail.com"
    },

    {
        "username": " vfq", 
        "email" : "vfq@gmail.com"
    },
    ]

for u in user:
    print(u["email"])