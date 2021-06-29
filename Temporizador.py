import time 
import os
h = m = s = 0 
hp = int(input('Hora de parada? '))
mp = int(input('Minuto de parada? '))
sp = int(input('Segubdo de parada?'))

while True:
    print('Parar em: {}:{}:{}'.format(hp,mp,sp))
    print(f'\n{h}:{m}:{s}')
    time.sleep(1)
    s +=1
    if s == 60:
        s = 0
        m +=1
    if m == 60:
        m = 0
        h +=1
    os.system('cls')
    if h == hp and m == mp and s == sp:
        print('\n{}:{}:{}'.format(h,m,s))
        print('Fim da contagem')
        break