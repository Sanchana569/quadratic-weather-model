import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Two real roots: {root1}, {root2}"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"One real root: {root}"
    else:
        return "Complex roots"

# Read input from file
with open("input.txt", "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    a, b, c = map(float, line.strip().split())
    result = solve_quadratic(a, b, c)
    print(f"Equation {i+1}: a={a}, b={b}, c={c} → {result}")
