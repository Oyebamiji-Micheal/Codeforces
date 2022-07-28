def checker(string):
    m = "hello"
    x = 0
    for i in range(len(string)):
        if string[i] == m[x]:
            x += 1
        if x == 5:
            return "YES"
    return "NO"


if __name__ == "__main__":
    string = input()
    x = checker(string)
    print(x)