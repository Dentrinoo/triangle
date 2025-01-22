# Input the coordinates of vertices A, B, C
ax = int(input('Введите координату X вершины A: '))  # Input X-coordinate of vertex A
ay = int(input('Введите координату Y вершины A: '))  # Input Y-coordinate of vertex A
bx = int(input('\nВведите координату X вершины B: '))  # Input X-coordinate of vertex B
by = int(input('Введите координату Y вершины B: '))  # Input Y-coordinate of vertex B
cx = int(input('\nВведите координату X вершины C: '))  # Input X-coordinate of vertex C
cy = int(input('Введите координату Y вершины C: '))  # Input Y-coordinate of vertex C

# Input the coordinates of point O
ox = int(input('\nВведите координату X точки O: '))  # Input X-coordinate of point O
oy = int(input('Введите координату Y точки O: '))  # Input Y-coordinate of point O

# Calculate the lengths of the sides of triangle ABC
dlab = ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5  # Length of side AB
dlac = ((ax - cx) ** 2 + (ay - cy) ** 2) ** 0.5  # Length of side AC
dlbc = ((cx - bx) ** 2 + (cy - by) ** 2) ** 0.5  # Length of side BC

# Calculate the distances from points A, B, C to point O
dlao = ((ax - ox) ** 2 + (ay - oy) ** 2) ** 0.5  # Distance from A to O
dlbo = ((bx - ox) ** 2 + (by - oy) ** 2) ** 0.5  # Distance from B to O
dlco = ((cx - ox) ** 2 + (cy - oy) ** 2) ** 0.5  # Distance from C to O

# Handle special cases to ensure valid input
if (dlab == dlac + dlbc) or (dlac == dlbc + dlab) or (dlbc == dlab + dlac):  # Check if all points lie on one line
    print('\nНеверный ввод, все точки лежат на 1 прямой')
elif ax == bx and ax == cx and ay == by and cy == ay:  # Check if all points coincide
    print('\nНеверный ввод, координаты всех 3 точек совпадают')
else:
    # Calculate vector components for sides AB, BC, AC
    abx = ((ax - bx) ** 2) ** 0.5  # Vector length for AB (x-component)
    aby = ((ay - by) ** 2) ** 0.5  # Vector length for AB (y-component)
    bcx = ((cx - bx) ** 2) ** 0.5  # Vector length for BC (x-component)
    bcy = ((cy - by) ** 2) ** 0.5  # Vector length for BC (y-component)
    acx = ((cx - ax) ** 2) ** 0.5  # Vector length for AC (x-component)
    acy = ((cy - ay) ** 2) ** 0.5  # Vector length for AC (y-component)
    
    # Find the shortest side of the triangle
    if dlab < dlbc and dlab < dlac:
        stor = dlab
    elif dlbc < dlab and dlbc < dlac:
        stor = dlbc
    else:
        stor = dlac

    # Calculate the semi-perimeter of triangle ABC
    p = (dlab + dlbc + dlac) / 2

    # Calculate the area of triangle ABC using Heron's formula
    s = (p * (p - dlab) * (p - dlac) * (p - dlbc)) ** 0.5

    # Calculate the height from the smallest angle
    h = s * 2 / stor

    # Determine the position of point O relative to lines AB, BC, AC
    k1 = (ax - ox) * (by - ay) - (bx - ax) * (ay - oy)  # Line AB
    k2 = (bx - ox) * (cy - by) - (cx - bx) * (by - oy)  # Line BC
    k3 = (cx - ox) * (ay - cy) - (ax - cx) * (cy - oy)  # Line AC

    # Determine the relative position of point O
    if (ax == ox and ay == oy) or (bx == ox and by == oy) or (cx == ox and cy == oy):  # O coincides with a vertex
        print('\nТочка O принадлежит одной из вершин координатного треугольника ABC')
    elif k1 == 0 or k2 == 0 or k3 == 0:  # O lies on a side of the triangle
        print('\nТочка О принадлежит одной из сторон координатного треугольника ABC')
    elif (k1 < 0 and k2 < 0 and k3 < 0) or (k1 > 0 and k2 > 0 and k3 > 0):  # O is inside the triangle
        print('\nТочка O лежит внутри координатного треугольника ABC')
    else:  # O is outside the triangle
        print('\nТочка O лежит вне координатного треугольника ABC')

    # Output the height, side lengths of triangle ABC
    print('\nВысота, проведенная из наименьшего угла координатного треугольника ABC: ', '{:4.3f}'.format(h))
    print('\nДлина стороны AB векторного координатного треугольника ABC: ', '{:4.3f}'.format(dlab),
          '\nДлина стороны BC векторного координатного треугольника ABC: ', '{:4.3f}'.format(dlbc),
          '\nДлина стороны AC векторного координатного треугольника ABC: ', '{:4.3f}'.format(dlac))

input('\n\n\n')  # Pause the program to display results
