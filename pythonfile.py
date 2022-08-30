import numpy as np
from scipy.optimize import minimize


def given_func(x):
    return (x[0] - x[1]) ** 2 + (x[1] + x[2] - 2) ** 2 + (x[3] - 1) ** 2 + (x[4] - 1) ** 2


def constraint_1(x):
    return x[0] + 3 * x[1]


def constraint_2(x):
    return x[2] + x[3] - 2 * x[4]


def constraint_3(x):
    return x[1] - x[4]


x_range = (-10, 10)
given_bounds = (x_range, x_range, x_range, x_range, x_range)

cons_1 = {'type': 'eq', 'fun': constraint_1}
cons_2 = {'type': 'eq', 'fun': constraint_2}
cons_3 = {'type': 'eq', 'fun': constraint_3}

given_constraints = [cons_1, cons_2, cons_3]

initial_guess_1 = [2, 3, -2, 4, 5]
initial_guess_2 = [1, 4, -1, 7, 1]

results_1 = minimize(given_func, initial_guess_1, method='SLSQP', bounds=given_bounds, constraints=given_constraints)
results_2 = minimize(given_func, initial_guess_2, method='SLSQP', bounds=given_bounds, constraints=given_constraints)

print('\033[1m' + 'Results with initial guess of x0 = [2,3,-2,4,5]' + '\033[0m')
print(results_1)
print('\033[1m' + 'Results with initial guess of x0 = [1,4,-1,7,1]' + '\033[0m')
print(results_2)
print('\033[1m' + 'Results are not sensitive to intial guess upto 3 decimal places' + '\033[0m')