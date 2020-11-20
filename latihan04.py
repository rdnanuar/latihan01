_list = [3,5,2,5,7,8,9,0]
_list02=["john", 'Luke', 'Dada']
_list.sort()
print(_list)
print(_list02.index('Luke'))

print(sum(_list))

x = 0
for i in _list:
    x += i
print(f"sum loop {x}" )

del _list02[0]

print(_list02)

def root_number(x):
    z = 0
    for y in str(x):
        z +=int(y)
    if z > 9:
        z = root_number(z)
        
    return z
    

print(root_number(1234))


def repeat_num(num):
    return num if num <10 else repeat_num(sum(map(int, str(num))))
print(repeat_num(1389))

class Hero:
    def __init__(self,name,level):
        self.name = name
        self.level = level
    def getName(self):
        return self.name
    
hero = Hero('One Punchman', '1')
print(hero.getName())

class calculator:
    def getPenjumlahan(a ,b):
        return a + b
    
    def getPengurangan(a ,b):
        return a - b

    def getPerkalian(a ,b):
        return a * b
print(calculator.getPenjumlahan(4,6))
print(calculator.getPengurangan(4,6))
print(calculator.getPerkalian(4,6))

def replace_char(word):
    x = ''
    for w in word:
        if word.count(w) > 1:
            x += ')'
    else:
        x += '('
    return x
print(replace_char('Hello'))