from random import randint

Array1D = []
peaks = 0

for i in range(0,10):
    Array1D.append(randint(1,10000))

print(Array1D)

for x in range(0, len(Array1D) - 1):
    if x == 0:
        if Array1D[1] <= Array1D[0]:
            print("Peak found at " + str(0))
            break
            peaks += 1
    elif x == len(Array1D) - 2:
        if Array1D[len(Array1D)-2] <= Array1D[len(Array1D) - 1]:
            print("Peak found at " + str(len(Array1D)))
            break
            peaks += 1
    else:
        if Array1D[x - 1] <= Array1D[x]  and Array1D[x + 1] <= Array1D[x]:
            print("Peak found at " + str(x))
            peaks += 1
            break
        else:
            x += 1

print(str(peaks) + ' peaks found')