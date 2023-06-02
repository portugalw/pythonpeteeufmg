print('WHILE')

i = 0
while i<10:
    print(i)
    i+=1

print('FOR de Array') 
for i in [0,'a', 2, 6]:
    print(i)

print('FOR de range - Cria um array de 0 a 10') 
for i in range(10):
    print(i)

print('FATORIAL COM WHILE') 

n = 9
f = 1
print(str(n) + '! = ', end='')
while n > 0:
    f *= n
    n -= 1
print(str(f))


print('FATORIAL COM FOR - range: 1, = começa de 1; n + 1 = 8 + 1. No range, é sempre de 0 a n - 1') 

n = 9
f = 1
print(str(n) + '! = ', end='')
for i in range(1, n +1):
    f *= i
    n -= 1
print(str(f))





