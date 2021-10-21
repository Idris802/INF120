# Del oppgave 1
import math as m

B = 50000
k = 0.2
t = 0

C = (B / 12) - 1

N = (B/(1+C*m.e**(-k*t)))
print('N = {} når C = {}'.format(N, C))

N_t = [[t, int(B/(1+C*m.e**(-k*t)))] for t in range(0, 60)]
print(N_t)

print('{:10s}{:>s}'.format('t[h]', 'N'))
print(12*'-')
for i in N_t:
    print(f'{i[0]:2d}{i[1]:10d}')

print()
# Del oppgave 2
print('GANGETABELLEN')
print(40*'-')
for i in range(1, 11):
    [print(j*i, end='\t') for j in range(1, 11)]
    print('\n')
