def fun(l, n):
    minim = 0
    maxim = len(l) - 1
    while minim <= maxim:
        cur = int((minim + maxim) / 2)

        if l[cur] == n:
            return True
        elif l[cur] > n:
            maxim = cur - 1
        else:
            minim = cur + 1
    return False

print(fun([2,5,7,8,3],5))
