print('3↑↑3=3^3^3^3=7x10^12')
print('x ↑*a b')
e1,e2,e3 = int(input('x= ')),int(input('a= ')),int(input('b= '))
if e2 > 0:
    t = e1
    print()
    g = (e3 ** (e2 - 1))
    for i in range(0,g):
        t **= e3
print(t)