def sol1(x, r_n=0):
    if x < 10:
        x += 1
        r_n += 1
        return sol1(x, r_n)
    else:
        return x, r_n

ex1 = 3
answer = sol1(ex1)
print(answer)
