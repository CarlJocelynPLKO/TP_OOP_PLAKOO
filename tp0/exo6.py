def f(terrain, x1, y1, x2, y2):
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    c = 0
    if terrain == "R":
        c = dist * 1.0
    elif terrain == "H":
        c = dist * 1.5
    elif terrain == "S":
        c = dist * 2.0
    else:
        c = dist * 3.0
    print("cout:", c)
    return c
#noms non explicites, parametre initilisé et pas de docstring, variable non initialise