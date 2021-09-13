from scipy.optimize import minimize


def objective(x):

    s = 0
    for i in range(4):
        k = i + 1
        s += (7 - k) * x[i]

    return s


def c1_gteq(x):
    s = 0
    for i in [1, 3, 4]:
        s += (5 - i) * x[i - 1]

    return s - 2


def c2_gteq(x):
    s = 0
    for i in [1, 2, 4]:
        s += (i - 5) * x[i - 1]

    return s - 3


b = (-2, 2)
bounds = (b, b, b, b)
con1 = {"type": "ineq", "fun": c1_gteq}

con2 = {"type": "ineq", "fun": c2_gteq}
cons = [con1, con2]

test = [0, -2, 0, 2]
print("test")
print(objective(test))


print("solution")
sol = minimize(objective, test, method="SLSQP", bounds=bounds, constraints=cons)

print(sol)
