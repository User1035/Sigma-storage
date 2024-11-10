# this entire script still does not work, Going to finish it soon
X_axis = 2
Y_axis = 2
running = True
notvalid = True
N = True
S = True
E = True
W = True
print("you wake up in an open chamber in a cavern deep underground, You only have a compass")
print("1 for north (up) 2 for east (right) 3 for south (down) and 4 for west (left)")
while running:
    while notvalid:
        direction = int(input(""))
        if direction == 1 and N:
            Y_axis = Y_axis - 1
            notvalid = False
        elif direction == 2 and E:
            X_axis = X_axis + 1
            notvalid = False
        elif direction == 3 and S:
            Y_axis = Y_axis + 1
            notvalid = False
        elif direction == 4 and W:
            X_axis = X_axis - 1
            notvalid = False
        else:
            print("invalid, please re-enter your chosen direction")
            notvalid = True
    notvalid = True
    print(X_axis, Y_axis)
    if Y_axis == 0:
        if X_axis == 0:
            print("you find an L junction, 2 for east (right) and 3 for south (down)")
            N = False
            S = True
            E = True
            W = False
        if X_axis == 1:
            print("you find a corridor, 2 for east (right) and 4 for west (left)")
            N = False
            S = False
            E = True
            W = True
        if X_axis == 2:
            print("you find a T junction, 2 for east (right) 3 for south (down) and 4 for west (left)")
            N = False
            S = True
            E = True
            W = True
        if X_axis == 3:
            print("you find a corridor, 2 for east (right) and 4 for west (left)")
            N = False
            S = False
            E = True
            W = True
        if X_axis == 4:
            print("you find an L junction, 3 for south (down) and 4 for west (left)")
            N = False
            S = True
            E = False
            W = True
    if Y_axis == 1:
        if X_axis == 0:
            print("you find a T junction, 1 for north (up) 3 for south (down) and 2 for east (right)")
            N = True
            S = True
            E = True
            W = False
        if X_axis == 1:
            print("you find a dead end, 4 for west (left)")
            N = False
            S = False
            E = False
            W = True
        if X_axis == 2:
            print("you find a corridor, 1 for north (up) and 3 for south (down)")
            N = True
            S = True
            E = False
            W = False
        if X_axis == 3:
            print("you find a dead end, 3 for south (down)")
            N = False
            S = True
            E = False
            W = False
        if X_axis == 4:
            print("you find a corridor, 1 for north (up) and 3 for south (down)")
            N = True
            S = True
            E = False
            W = False
    if Y_axis == 2:
        if X_axis == 0:
            print("you find a corridor, 1 for north (up) and 3 for south (down)")
            N = True
            S = True
            E = False
            W = False
        if X_axis == 1:
            print("you find an L junction, 2 for east (right) and 3 for south (down)")
            N = False
            S = True
            E = True
            W = False
        if X_axis == 2:
            print("An open chamber, 1 for north (up) 2 for east (right) 3 for south (down) and 4 for west (left)")
            N = True
            S = True
            E = True
            W = True
        if X_axis == 3:
            print("you find a T junction, 1 for north (up) 3 for south (down) and 4 for west (left)")
            N = True
            S = True
            E = False
            W = True
        if X_axis == 4:
            print("you find a dead end, 1 for north (up)")
            N = True
            S = False
            E = False
            W = False
    if Y_axis == 3:
        if X_axis == 0:
            print("you find a corridor, 1 for north (up) and 3 for south (down)")
            N = True
            S = True
            E = False
            W = False
        if X_axis == 1:
            print("you find a dead end, 1 for north (up)")
            N = True
            S = False
            E = False
            W = False
        if X_axis == 2:
            print("you find a corridor, 1 for north (up) and 3 for south (down)")
            N = True
            S = True
            E = False
            W = False
        if X_axis == 3:
            print("you find a corridor, 1 for north (up) and 3 for south (down)")
            N = True
            S = True
            E = False
            W = False
        if X_axis == 4:
            print("you find a dead end, 3 for south (down)")
            N = False
            S = True
            E = False
            W = False
    if Y_axis == 4:
        if X_axis == 0:
            print("you find an L junction, 1 for north (up) and 2 for east (right)")
            N = True
            S = False
            E = True
            W = False
        if X_axis == 1:
            print("you find a dead end, 4 for west (left)")
            N = False
            S = False
            E = False
            W = True
        if X_axis == 2:
            print("you find an L junction, 1 for north (up) and 2 for east (right)")
            N = True
            S = False
            E = True
            W = False
        if X_axis == 3:
            print("you find a T junction, 1 for north (up) 2 for east (right) and 4 for west (left)")
            N = True
            S = False
            E = True
            W = True
        if X_axis == 4:
            print("you find an L junction, 1 for north (up) and 4 for west (left)")
            N = True
            S = False
            E = False
            W = True
