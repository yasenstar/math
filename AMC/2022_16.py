import sympy as sp

def solve_equations():
    try:
        m = sp.symbols('m')

        eq = sp.Eq(2**m * (1/4096)**0.5, 2 * (1/4096)**(1/m))

        solutions = sp.solve((eq), (m), dict=True)

        print("解的列表:", solutions)

    except Exception as e:
        print(f"求解时发生错误: {e}")

if __name__ == "__main__":
    solve_equations()