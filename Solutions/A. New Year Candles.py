def checker(a, b):
    if b > a:
        return a
    res = 0
    while a >= b:
        quotient = int(a/b)
        rem = a%b
        a = quotient + rem
        res += quotient * b

    return res + a
    

if __name__ == "__main__":
    a, b = map(int, input().split())
    ans = checker(a, b)
    print(ans)
