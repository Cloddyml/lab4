import random


def quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        i = random.choice(a)
    l = [n for n in a if n < i]
    d = [i] * a.count(i)
    r = [n for n in a if n > i]
    return quick_sort(l) + d + quick_sort(r)


def r_sort(a):
    s = len(a)
    w = True
    while s > 1 or w:
        s = max(1, int(s/1.247))
        w = False
        for j in range((len(a)) - s):
            g = j + s
            if a[j] > a[g]:
                a[j], a[g] = a[g], a[j]
                w = True
    return a
