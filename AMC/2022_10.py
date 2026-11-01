import sympy as sp

def solve_equations():
    try:
        a, b = sp.symbols('a b')

        eq1 = sp.Eq(a**2 + b**2, 64)
        eq2 = sp.Eq((a - 2)**2 + (b - 2)**2, 32)

        solutions = sp.solve((eq1, eq2), (a, b), dict=True)

        print("解的列表:", solutions)

        # 使用 sp.simplify() 将乘积式化简为最终数值
        area = sp.simplify(solutions[0][a] * solutions[0][b])
        print("计算得到的矩形面积:", area)

    except Exception as e:
        print(f"求解时发生错误: {e}")

if __name__ == "__main__":
    solve_equations()