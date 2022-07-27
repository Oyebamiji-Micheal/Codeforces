def checker(string):
    string = string.lower()
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    res = []

    for i in string:
        if i not in vowels:
            res.append('.')
            res.append(i)

    return ''.join(res)


if __name__ == '__main__':
    string = input()
    x = checker(string)
    print(x)
