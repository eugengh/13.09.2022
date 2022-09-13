from msilib.schema import Error


from aifc import Error
n = int(input('Cate elem contine lista ta ? '))
def listaint(x):
    lista = []
    for i in range(x):
        try:
            ele = int(input('Elementul ' + str(i+1)+' este '))
        except ValueError:
            raise Error('Nu este int')
        lista.append(ele)
    return print(lista)

listaint(n)

m = int(input('Cate elem contine lista a doua ? '))
def listafloat(y):
    lista = []
    for i in range(y):
        try:
            ele = float(input('Elementul ' + str(i+1)+' este '))
        except ValueError:
            raise Error('Nu este float')
        lista.append(ele)
    return print(lista)

listafloat(m)

