# Example with constraints
from scipy.optimize import minimize

# Define the objective function
def objective(x):
    return x[0]**2 + x[1]**2

# Define the constraint
def constraint(x):
    return x[0] + x[1] - 1

# Initial guess
x0 = [0.5, 0.5]

# Define the constraint dictionary
constraint_dict = {'type': 'eq', 'fun': constraint}

# Perform the optimization with the constraint
result = minimize(objective, x0, constraints=constraint_dict)

# Print the result
print(result)
