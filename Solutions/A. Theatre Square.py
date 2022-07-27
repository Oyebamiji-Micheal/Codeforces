from math import ceil

def checker(n, m, s):
    length = ceil(n/s)  
    breadth = ceil(m/s)
    return length * breadth

if __name__ == '__main__':
    n, m, s = map(int, input().split())
    ans = checker(n, m, s)
    print(ans)
