from matplotlib import pyplot as plt
import math

plt.grid()
plt.gca().set_aspect("equal")
plt.axis([-10, 10, -10, 10])


def gen_hex(edges, angles, start):
    
    angles_rad = [math.radians(angle) for angle in angles ]
    a, b, c, d, e = edges[0], edges[1], edges[2], edges[3], edges[4]
    A, B, C, D, E = angles_rad[0], angles_rad[1], angles_rad[2], angles_rad[3], angles_rad[4]

    p = []

    p.append((start))
    p.append((p[0][0] + a * math.cos(math.pi - A), p[0][1] + a * math.sin(math.pi - A)))
    p.append((p[1][0] - b * math.cos(A + B - math.pi), p[1][1] + b * math.sin(A + B - math.pi)))
    p.append((p[2][0] - c * math.cos(A + B + C - math.pi * 2), p[2][1] + c * math.sin(A + B + C - math.pi * 2)))
    p.append((p[3][0] - d * math.cos(math.pi * 3 - (A + B + C + D)), p[3][1] - d * math.sin(math.pi * 3 - (A + B + C + D))))
    p.append((p[4][0] + e * math.cos(A + B + C + D + E - math.pi * 3), p[4][1] - e * math.sin(A + B + C + D + E - math.pi * 3)))

    x = []
    y = []
    for point in p:
        x.append(point[0])
        y.append(point[1])
    
    x.append(p[0][0])
    y.append(p[0][1])
    plt.plot(x, y)

    new_angles = [angle for angle in angles]
    new_angles[0] = angles[0] + math.degrees(math.atan((p[0][1] - p[5][1]) / (p[0][0] - p[5][0])))
    new_angles.append(720 - new_angles[0] - new_angles[1] - new_angles[2] - new_angles[3] - new_angles[4])
    
    new_edges = [edge for edge in edges]
    new_edges.append(math.sqrt((p[0][0] - p[5][0]) ** 2 + (p[0][1] - p[5][1]) ** 2))

    return p, new_angles, new_edges


def gen_type1_angles(): # a = d, B + C + D = 2pi
    angles_set = []

    for B in range(100, 161, 2):
        for C in range(100, 161, 2):
            D = 360 - B - C
            if D < 100:
                continue
            for E in range(100, 161, 2):
                for A in range(100, 161, 2):
                    F = 360 - E - A
                    if F < 100:
                        continue
                    
                    angles_set.append([A, B, C, D, E])
                    
    return angles_set
        


# def gen_type2(): # a = d, c = e, B + C + D = 2pi
#     pass


# def gen_type3(): # a = b, c = d, e = f, B = D = F = 2pi/3
#     pass


gen_hex([2, 1, 2, 2, 1], [120, 120, 120, 120, 120], (-2, 0))
gen_hex([3, 2, 1, 3, 2], [120, 120, 120, 120, 120], (4, 0))

points, angles, edges = gen_hex([2, 4, 1, 4, 3], [120, 120, 120, 120, 120], (-5, -5))
print(points, angles, edges)

plt.show()

# print(gen_type1_angles())