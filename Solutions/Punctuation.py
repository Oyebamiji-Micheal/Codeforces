def checker(text):
    res = ''
    for i in text:
        if i.isalpha():
            res += i
            space = True
        elif i == ' ' and space:
            res += i
            space = False
        elif i == '.' or i == ',' or i == '!' or i == '?':
            if not space:
                res = res.rstrip()
            res += i
            res += ' '
            space = False

    return res

if __name__ == '__main__':
    ans = checker(input())
    print(ans)
