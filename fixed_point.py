
def fixed_point_iter():
    x = 0
    ea = 0
    curr = 0
    prev = 0

    for val in range(15):
        x = round(curv(x), 6)
        curr = x

        if curr != 0:
            ea = abs(round((curr-prev)/curr*100, 2))

        print(x, 'error estimate'.title(), ea)
        prev = curr

        if ea < 0.5:
            break
