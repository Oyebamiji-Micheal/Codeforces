def checker(x):
    res = ''
    if x[0] == '9':
        res += '9'
        x = x[1:]
        
    for num in x:
        if int(num) >= 5:
            res += str(9 - int(num))
        else:
            res += num

    return res

if __name__ == "__main__":
    x = input()
    res = checker(x)
    print(res)
