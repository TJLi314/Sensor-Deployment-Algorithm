from matplotlib import pyplot as plt
import math 

plt.grid()
plt.gca().set_aspect("equal")
plt.axis([-3, 5, -2, 4])

def kpp_algorithm(k, d): # calculates optimal point placement of k points with minimum d separation

    points = []
    for n in range(k):      # Place k amount of points
        next_point = get_triangle_point(points, d)
        points.append(next_point)

    print(points)
    for point in points:    # Plot the points
        plt.plot(point[0], point[1], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")

    return points

def get_triangle_point(points, d): # Returns the next triangulation point for the given point placement and min distance
    if len(points) == 0:  # two base cases
        return (0, 0)
    
    if len(points) == 1:
        x = points[0][0] + d
        y = points[0][1]
        return (x, y)
    
    print(points)
    poss_points = []        # Add all possible triangulation points
    for p1 in range(len(points) - 1):
        for p2 in range(p1 + 1, len(points)):
            print(points[p1], points[p2])
            if abs(dist(points[p1], points[p2]) - d) < 0.0000000001:
                print(dist(points[p1], points[p2]))
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
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    x_mid, y_mid = (x1 + x2) / 2, (y1 + y2) / 2
    h = d * math.sqrt(3) / 2

    if y1 == y2:
        return (x_mid, y_mid + h), (x_mid, y_mid - h)
    else:
        slope = -(x2 - x1) / (y2 - y1)
    
    n = math.sqrt((h ** 2) / (slope ** 2 + 1))
    return (x_mid + n, y_mid + n * slope), (x_mid - n, y_mid - n * slope)

def in_points(p, points): # returns whether a point is in the set of points
    
    for point in points:
        if abs(p[0] - point[0]) < 0.000000001 and abs(p[1] - point[1]) < 0.000000001:
            return True
    return False

def dist(p1, p2): # Calculates distance between two points
    return math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))

def get_width(points): # finds width of the given point placement
    two_points = (None, None)
    width = float('-inf')

    for p1 in range(len(points) - 1):
        for p2 in range(p1, len(points)):
            if dist(points[p1], points[p2]) > width:
                width = dist(points[p1], points[p2])
                two_points = (points[p1], points[p2])

    return width, two_points

points = kpp_algorithm(20, 1)
print(points)

width, two_points = get_width(points)
print(width)
print(two_points)

plt.show()


