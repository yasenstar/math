import sympy as sp

def solve_equations():
    try:
        x = sp.symbols('x')

        eq = sp.Eq(10*x**3-39*x**2+29*x-6, 0)

        solutions = sp.solve((eq), (x), dict=True)

        print("解的列表:", solutions)

        print((solutions[0][x]+2)*(solutions[1][x]+2)*(solutions[2][x]+2))

    except Exception as e:
        print(f"求解时发生错误: {e}")

if __name__ == "__main__":
    solve_equations()


    