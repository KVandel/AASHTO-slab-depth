import numpy as np
from scipy.optimize import fsolve
#this is my test 1
ZR = -1.645
SO = 0.34
W18 = 15907.62
TSI = 2.5
delta_PSI = 2
Sc = 531
Cd = 1
J = 3.2
Ec =3.6e10
k = 362

def equation(D) :
    logW18_part1 = ZR * SO + 7.35 * np.log10(D +1) - 0.06

    logW18_part2 = np.log10(delta_PSI/3.0) / (1+(1.624e7/ (D +1)**8.46))

    term1 = (4.22 - 0.32 * TSI) * np.log10(Sc * Cd * (D**0.75-1.132))
    term2 = (215.63 * J * D**0.75) - (18.42/(Ec/k)**0.25)

    logW18 = logW18_part1 + logW18_part2 + term1 / term2
    return  10**logW18 - W18

initial_guess = 10
D_solution = fsolve(equation,initial_guess)
print(f'The motherfucking answer of D(slab thickness) issssss :{D_solution[0]:.2f} inches')