"""
Topics:
    divmod
    integertoArray
"""

def get_digits(n):
    try:
        digits = []
        while(n>=1):
            digits.append(int(n%10))
            n = int(n/10)
        return digits
    except ZeroDivisionError:
        print('Zero division error')


def findDigits(n):
    if n == 0:
        return 0

    digits = get_digits(n)
    count = 0
    for digit in digits:
        try:
            if not n%digit == 0:
                continue
            count += 1
        except ZeroDivisionError:
            continue
    return count


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = findDigits(n)
        print(result)

