def nestedsquare():
    for i in range(7):
        for j in range(7):
            if i == 0:
                print("*", end="")
            else:
                print(" ", end="")