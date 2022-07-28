def checker():
    num = int(input())
    lucky = [4, 47, 447, 474, 477, 444, 7, 74, 774, 747, 744, 777]
    if num in lucky:
        return "YES"
    else:
        for i in lucky:
            if num % i == 0:
                return "YES"
    
    return "NO"

if __name__ == "__main__":
    x = checker()
    print(x)