X_axis = 5
Y_axis = 5
running = True
X_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while running:
    direction = int(input("1 for north (up) 2 for east (right) 3 for south (down) and 4 for (left)"))
    if direction == 1:
        Y_axis = Y_axis + 1
    elif direction == 2:
        X_axis = X_axis + 1
    elif direction == 3:
        Y_axis = Y_axis - 1
    elif direction == 4:
        X_axis = X_axis - 1
    print(Y_array[Y_axis], X_array[X_axis])
