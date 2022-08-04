def checker(s, t, p):
    j = 0
    hashmap = {}
    
    for i in t:
        if j < len(s) and i == s[j]:
            j += 1
        elif i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
            
    if j < len(s):
        return 'NO'
    
    for i in p:
        if i in hashmap and hashmap[i] > 0:
            hashmap[i] -= 1

    for val in hashmap.values():
        if val > 0:
            return 'NO'

    return 'YES'

if __name__ == '__main__':
    query = int(input())
    for _ in range(query):
        s = input()
        t = input()
        p = input()  
        ans = checker(s, t, p)
        print(ans)
