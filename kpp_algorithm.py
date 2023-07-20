from matplotlib import pyplot as plt
import math
from welzl_algorithm import Point
from welzl_algorithm import dist

# plt.grid()
# plt.axis([-1, 1.5, -1, 1.5])
# plt.gca().set_aspect("equal")


def kpp_algorithm(k, d): # calculates optimal point placement of k points with minimum d separation

    if k == 4:
        points = [Point(0, 0), Point(d, 0), Point(0, d), Point(d, d)]
    elif k == 5:
        points = pentagon(d)
    else:
        points = []
        for _ in range(k):      # Place k amount of points
            next_point = get_triangle_point(points, d)
            points.append(next_point)

    # for point in points:    # Plot the points
    #     plt.plot(point.X, point.Y, marker="o", markersize=20, markeredgecolor="red", markerfacecolor="green")

    return points

def get_triangle_point(points, d): # Returns the next triangulation point for the given point placement and min distance
    if len(points) == 0:  # two base cases
        return Point(0, 0)
    
    if len(points) == 1:
        return Point(d, 0)
    
    poss_points = []        # Add all possible triangulation points
    for p1 in range(len(points) - 1):
        for p2 in range(p1 + 1, len(points)):
            if abs(dist(points[p1], points[p2]) - d) < 0.0000000001:
                trian1, trian2 = triangulate(points[p1], points[p2], d)
                
                if not in_points(trian1, points):
                    poss_points.append(trian1)
                if not in_points(trian2, points):
                    poss_points.append(trian2)
    
    min_width = float('inf')
    poss_point = None
    for point in poss_points:   # Return the triangulation point that yields the lowest width for every possible placement
        width = get_width(points + [point])[0]
        if width < min_width:
            min_width = width
            poss_point = point
    
    return poss_point

def triangulate(p1, p2, d): # Returns the two possible triangulation points given two points
    x1, y1, x2, y2 = p1.X, p1.Y, p2.X, p2.Y
    x_mid, y_mid = (x1 + x2) / 2, (y1 + y2) / 2
    h = d * math.sqrt(3) / 2

    if y1 == y2:
        return Point(x_mid, y_mid + h), Point(x_mid, y_mid - h)
    else:
        slope = -(x2 - x1) / (y2 - y1)
    
    n = math.sqrt((h ** 2) / (slope ** 2 + 1))
    return Point(x_mid + n, y_mid + n * slope), Point(x_mid - n, y_mid - n * slope)

def in_points(p, points): # returns whether a point is in the set of points
    
    for point in points:
        if abs(p.X - point.X) < 0.000000001 and abs(p.Y - point.Y) < 0.000000001:
            return True
    return False

def pentagon(d): # returns the points of a regular pentagon with edge length d
    # a = Point(0, 0)
    # b = Point(d, 0)
    # c = Point(d + d * math.cos(math.radians(72)), d * math.sin(math.radians(72)))
    # e = Point(c.X - d * math.cos(math.radians(36)), c.Y + d * math.sin(math.radians(36)))
    # f = Point(-d * math.cos(math.radians(72)), d * math.sin(math.radians(72)))
    a = Point(-0.25, -0.5)
    b = Point(a.X + d, -0.5)
    c = Point(b.X + d * math.cos(math.radians(72)), b.Y + d * math.sin(math.radians(72)))
    e = Point(c.X - d * math.cos(math.radians(36)), c.Y + d * math.sin(math.radians(36)))
    f = Point(a.X - d * math.cos(math.radians(72)), a.Y + d * math.sin(math.radians(72)))
    return [a, b, c, e, f]


def get_width(points): # finds width of the given point placement
    two_points = [None, None]
    width = float('-inf')

    for p1 in range(len(points) - 1):
        for p2 in range(p1, len(points)):
            if dist(points[p1], points[p2]) > width:
                width = dist(points[p1], points[p2])
                two_points = [points[p1], points[p2]]

    return width, two_points

def print_points(points): # Prints the point set
    s = "Points: "
    for point in points:
        s += "(" + str(point.X) + ", " + str(point.Y) + ") "
    print(s)

# points = kpp_algorithm(5, 1)
# print_points(points)

# width, two_points = get_width(points)
# print(width)
# print_points(two_points)

# # plt.plot(0, -0.5, marker="o", markersize=10, markeredgecolor="red", markerfacecolor="green")
# # plt.plot(0, 0.5, marker="o", markersize=10, markeredgecolor="red", markerfacecolor="green")
# # plt.plot(1, -0.5, marker="o", markersize=10, markeredgecolor="red", markerfacecolor="green")
# # plt.plot(1, 0.5, marker="o", markersize=10, markeredgecolor="red", markerfacecolor="green")

# plt.show()


