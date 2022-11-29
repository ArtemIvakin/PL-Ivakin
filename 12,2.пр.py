def strmax():
    a = int(input())
    if a == 0:
        return 1
    return max(a, strmax())
print(strmax())