def checker():
    res = []
    a = int(input())
    b = int(input())
    c = int(input())

    res.append(a + b + c)
    res.append(a + b * c)
    res.append(a * b + c) 
    res.append(a * b * c)
    res.append((a + b) * c) 
    res.append(a * (b + c))

    print(res)
    return max(res)
    
if __name__ == "__main__":
    x = checker()
    print(x)