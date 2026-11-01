import sympy as sp

def solve_equations():
    try:
        x1, x2, x3 = sp.symbols('x1 x2 x3')

        eq1 = sp.Eq(x1 + x2 + x3, 96)
        eq2 = sp.Eq(x1, 6 * x3)
        eq3 = sp.Eq(x2 - 40, x3)

        solutions = sp.solve((eq1, eq2, eq3), (x1, x2, x3), dict=True)

        if solutions:
            print("Solutions found:")
            for sol in solutions:
                print(f"x1 = {sol[x1]}, x2 = {sol[x2]}, x3 = {sol[x3]}")
                print("answer = ",abs(sol[x1]-sol[x2]))
        else:
            print("No solutions found.")

    except Exception as e:
        print(f"Error while solving equations: {e}")

if __name__ == "__main__":
    solve_equations()

# Answer: E