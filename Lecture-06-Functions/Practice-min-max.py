def calc_min(x, y, *z):
    res = x if x < y else y
    for i in z:
        if res > i:
            res = i
    return res

def calc_max(x, y, *z):
    res = x if x > y else y
    for i in z:
        if res < i:
            res = i
    return res

print(calc_min(7, 4))
print(calc_min(7, 4, 8))
print(calc_min(7, 4, 8, 3))
print(calc_min(7, 4, 8, 3, 1))

print(calc_max(7, 4))
print(calc_max(7, 4, 8))
print(calc_max(7, 4, 8, 3))
print(calc_max(7, 4, 8, 3, 11))
