def checker():
    string = input()
    if string.isupper():
        return string.lower()
    elif string[0].islower():
        if string[1:].isupper() or not string[1:]:
            return string.capitalize()
    return string
    
if __name__ == "__main__":
    x = checker()
    print(x)