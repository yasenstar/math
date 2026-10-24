import math

def is_perfect_square(n):
    if n < 0:
        return False
    sqrt = math.isqrt(n)
    return sqrt * sqrt == n

number = 2
print(number)
result = False
while result==False:
    if is_perfect_square(number):
        count = 0
        for i in range(1,number+1):
            if number/i == int(number/i):
                print(number/i)
                count = count + 1
        print(count)
        if is_perfect_square(count):
            result = True
        else:
            number = number + 1
    else:
        number = number + 1

print(number)