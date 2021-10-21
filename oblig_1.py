import math as m

# a)
B = 50000
k = 0.2
t = 0

N_5k = [(B/(1+C*m.e**(-k*t)), C) if B/(1+C*m.e**(-k*t)) == 5000 else "not" for C in range(1, 10)]
print("N = {}, when C = {}".format(N_5k[-1][0], N_5k[-1][1]))


# b)

# From task a we know that C is 9 when N is 5000.

C = 9
t = 24
N_24 = B/(1+C*m.e**(-k*t))
print("Population after 24 hours is {}".format(N_24))

# c)

N_90_rough_estimate = [(B / (1 + C * m.e ** (-k * t)), t) if 45100 >= B / (1 + C * m.e ** (-k * t)) >= 44900 else t for t in range(1, 25)]
print("after about {} hours the population has reached {} which is almost 90% of B".format(N_90_rough_estimate[-3][1], N_90_rough_estimate[-3][0]))
