from re import M


def putere():
    suma = 1
    for i in range(2, 9, 2):
        suma+= 0.5**i
    return suma

print(putere())
