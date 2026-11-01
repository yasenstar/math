def solve_repeating_decimal_problem():
    valid_numbers = []

    # Iterate over all non-zero digits for a, b, and c
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                # Simplified condition derived from: 0.abc_bar = 1/3 * (0.a_bar + 0.b_bar + 0.c_bar)
                if 7 * a == 3 * b + 4 * c:
                    number = 100 * a + 10 * b + c
                    valid_numbers.append((number, a, b, c))

    print(f"Total count of valid numbers: {len(valid_numbers)}")
    print("\nMatching 3-digit integers (abc):")
    for num, a, b, c in valid_numbers:
        print(f"  {num}  -->  7*({a}) = 3*({b}) + 4*({c})")

if __name__ == "__main__":
    solve_repeating_decimal_problem()