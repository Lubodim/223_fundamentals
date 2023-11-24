def c_m(r_c):
    matr = []
    for row in range(r_c):
        matr.append([])
        for col in range(r_c):
            matr[row].append(col +1 + row * r_c)

    return matr