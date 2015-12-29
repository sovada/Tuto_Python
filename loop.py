while 1:
    nb = input("Quelle table de multiplication? (press Q or q to exit)")

    if nb == "Q" or (nb == "q"):
        break
    else:
        nb = int(nb)
        i  = 0

        while i <= 10:
            print(nb, " X ", i, " = ", nb*i)
            i+=1
