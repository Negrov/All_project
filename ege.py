rev = [1000, 1, -1]
simp = [1, 1000]
for A in range(*rev):
    count = 1
    for x in range(0, 1000):
        for y in range(0, 5000):
            count *= (2*y+x != 70) or (x < y) or (A < x)
            if not count:
                break
    if  count :
        print(A)
        break