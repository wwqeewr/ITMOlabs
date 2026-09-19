def factorial_to_decimal(digits: str) -> int:
    result = 0
    weight = 1
    for i, ch in enumerate(reversed(digits), start=1):
        weight *= i
        digit = int(ch)
        result += digit * weight
    return result

def decimal_to_fibonacci(n: int) -> str:
    fibs = [1, 2]
    while fibs[-1] + fibs[-2] <= n:
        fibs.append(fibs[-1] + fibs[-2])

    digits = []
    remainder = n
    for f in reversed(fibs):
        if f <= remainder:
            digits.append('1')
            remainder -= f
        else:
            digits.append('0')

    result = ''.join(digits).lstrip('0')
    return result

def decimal_to_balanced9(n: int) -> list:
    if n == 0:
        return [0]
    digits = []
    m = n
    while m != 0:
        r = m % 9
        if r > 4:
            r -= 9
        m = (m - r) // 9
        digits.append(r)
    digits.reverse()
    return digits

def balanced9_to_str(digits: list) -> str:
    return ' '.join(f'{d:+d}' if d != 0 else '0' for d in digits)
    
def negabase10_to_decimal(digits: str) -> int:
    result = 0
    for i, ch in enumerate(reversed(digits)):
        d = int(ch)
        result += d * ((-10) ** i)
    return result

print('10', factorial_to_decimal('622111'))
print('11', decimal_to_fibonacci(915))
print('12', balanced9_to_str(decimal_to_balanced9(18205)))
print('13', negabase10_to_decimal('923'))
