a = 2
print(a,"относится к типу", type(a))

b = 15.0001
print(b,"относится к типу", type(b))

c = 1+2j
print(c,"Комплексное число?", isinstance(c,complex))

print(6//2)

def puk_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d

print(puk_arg(d='1',b='2',c='3',a='4'))

def arg(v=(1,2,3,4)):
    return v[0]
print(arg())

def s(r,pi=3.14159):
    return pi * r * r
print(s(2))

def lenght(u: str = '') -> str:
    return len(u)
print(lenght())


def liist(f: list = [], m: list=[]) -> int:
    return max(len(f),len(m))
print(liist([2,5,6],[4,6,7,8,9]))


def liiist(f: list, m: str) -> list:
    f.append(m)
    return f
print(liiist([8],'стр'))

def listik(z: list) -> int:
    return sum(z)
print(listik([8,4,6]))