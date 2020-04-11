def divide(dividend: int, divisor: int):
    test = 5
    print("test", test)
    test = -test
    print("new test ", test)
    if dividend == 0: return 0

    odd = False
    if dividend < 0 and divisor < 0:
        odd = False
        dividend = -dividend
        divisor = -divisor
    elif dividend > 0 and divisor > 0:
        odd = False
    else:
        odd = True
        if dividend < 0:    dividend = -dividend
        else:               divisor = -divisor
    output = 0
    while dividend - divisor >= 0:
        dividend = dividend - divisor
        output += 1
        print(output)

    if odd: output = -output

    return output
print(divide (-2147483648, -1))