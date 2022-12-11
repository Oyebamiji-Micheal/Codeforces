def checker(n, s):

    if not s:
        return n

    if not n:
        return ''

    s = sorted(s, reverse=True)
    n_pointer = 0
    s_pointer = 0
    res = ''
    
    while n_pointer < len(n) and s_pointer < len(s):
        if s[s_pointer] > n[n_pointer]:
            res += s[s_pointer]        
            s_pointer += 1
            n_pointer += 1
        else:
            res += n[n_pointer]
            n_pointer += 1

    return res + n[n_pointer:]


if __name__ == "__main__":
    n = input()
    s = input()
    res = checker(n, s)
    print(res)
