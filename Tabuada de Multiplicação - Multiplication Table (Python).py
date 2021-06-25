#Tabuada simples em Python
print('Tabuada de 2 até 10\n')
print('\033[32mTabuada de 2:')
for n in range(11):
    print('{:2} x 2 = {}'.format(n,n*2))
print('\033[33mTabuada de 3:')
for n in range (11):
    print('{:2} x 3 = {}'.format(n, n*3))
print('\033[34mTabuada de 4:')
for n in range (11):
    print('{:2} x 4 = {}'.format(n,n*4))
print("\033[35mTabuada de 5:")
for n in range (11):
    print('{:2} x 5 = {}'.format(n,n*5))
print('\033[36mTabuada de 6:')
for n in range(11):
    print('{:2} x 6 = {}'.format(n,n*6))
print('\033[37mTabuada de 7:')
for n in range(11):
    print("{:2} x 7 = {}".format(n,n*7))
print('\033[31mTabuada de 8:')
for n in range (11):
    print('{:2} x 8 = {}'.format(n,n*8))
print('\033[39mTabuada de 9:')
for n in range (11):
    print('{:2} x 9 = {}'.format(n,n*9))
print('\033[30mTabuada de 10:')
for n in range (11):
    print('{:2} x 10 = {}'.format(n,n*10))

