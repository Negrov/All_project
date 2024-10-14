count = 0
for i in range(1000000000, 9999999999):
    if all([str(i).count(str(j)) == 1 for j in range(10)]):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i, flush=True)
            count += 1

