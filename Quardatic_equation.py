import math

def quadratic_solver(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

def main():
    print("Quadratic Equation Solver")
    print("Enter coefficients for ax^2 + bx + c = 0")

    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        roots = quadratic_solver(a, b, c)

        print("Roots of the equation:")
        print(f"Root 1: {roots[0]}")
        print(f"Root 2: {roots[1]}")
    except ValueError:
        print("Please enter valid numerical coefficients.")


