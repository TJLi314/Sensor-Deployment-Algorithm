from matplotlib import pyplot as plt
import math 
from random import randint

# plt.grid()
# plt.gca().set_aspect("equal")
# plt.axis([-3, 5, -2, 4])

class Point: # Class to represent a 2D point on a coordinate grid
    def __init__(self, X = 0, Y = 0) -> None:
        self.X = X
        self.Y = Y
    
class Circle: # Class to represent a 2D circle on a coordinate grid
    def __init__(self, center = Point(), R = 0) -> None:
        self.center = center
        self.radius = R

def dist(a, b): # Returns distance between two points
    return math.sqrt(math.pow((a.X - b.X), 2) + math.pow((a.Y - b.Y), 2))

def is_inside(point, circle): # Checks whether a point lies on inside or on the boundaries of a circle
    return dist(point, circle.center) <= circle.radius

def circle_from2(A, B): # Returns the smallest circle that intersects two points
    center = Point((A.X + B.X) / 2.0, (A.Y + B.Y) / 2.0 )
    return Circle(center, dist(A, B) / 2.0 )

def get_circle_center(bx, by, cx, cy): # Helper method to get a circle defined by 3 points
    B = bx * bx + by * by
    C = cx * cx + cy * cy
    D = bx * cy - by * cx
    return Point((cy * B - by * C) / (2 * D), (bx * C - cx * B) / (2 * D))

def circle_from3(A, B, C): # Returns a circle that intersects all three points
    I = get_circle_center(B.X - A.X, B.Y - A.Y, C.X - A.X, C.Y - A.Y)
  
    I.X += A.X
    I.Y += A.Y
    return Circle(I, dist(I, A))

def is_valid_circle(circle, points): # Checks if a circle encloses the given points
    for p in points:
        if not is_inside(p, circle):
            return False
    return True

def base_case_circle(R): # Returns the minimum enclosing circle for boundary points <= 3
    if not R:
        return Circle()
    elif len(R) == 1:
        return Circle(R[0], 0)
    elif len(R) == 2:
        return circle_from2(R[0], R[1])

    for i in range(3):
        for j in range(i + 1, 3):
            circle = circle_from2(R[i], R[j])
            
            if is_valid_circle(circle, R):
                return circle
    return circle_from3(R[0], R[1], R[2])

def welzl_algorithm(points, R = None): # Returns the minimum enclosing circle using welzl's algorithm
    if R == None:
        R = []

    if len(points) == 0 or len(R) == 3: # Base case
        return base_case_circle(R)
    
    index = randint(0, len(points) - 1) # Select a random point
    p = points[index]

    new_points = [point for point in points]
    new_points.pop(index)       # delete the selectd random point from the new points

    # get minimum enclosing circle for the set of points minus the random point
    min_enc_circle = welzl_algorithm(new_points, [r for r in R]) 
    
    if not is_inside(p, min_enc_circle):
        R.append(p)
        min_enc_circle = welzl_algorithm(new_points, [r for r in R])
    
    return min_enc_circle

def point_generator(num, x_min, x_max, y_min, y_max):
    plt.grid()
    plt.gca().set_aspect("equal")
    plt.axis([x_min * 1.5, x_max * 1.5, y_min * 1.5, y_max * 1.5])

    points = []
    for _ in range(num):
        x = randint(x_min, x_max)
        y = randint(y_min, y_max)

        plt.plot(x, y, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
        points.append(Point(x, y))

    return points    

mec = welzl_algorithm(point_generator(25, -10, 10, -10, 10))
print("Center = {",mec.center.X,",",mec.center.Y,"} Radius =",mec.radius)

plt.plot(mec.center.X, mec.center.Y, marker="o", markersize=5, markeredgecolor="pink", markerfacecolor="blue")
circle = plt.Circle((mec.center.X, mec.center.Y), mec.radius, fill = False)

# mec = welzl_algorithm([Point(0, 0), Point(0, 1), Point(1, 0)])
# print("Center = {",mec.center.X,",",mec.center.Y,"} Radius =",mec.radius)
# circle = plt.Circle((mec.center.X, mec.center.Y), mec.radius, fill = False)
# plt.plot(0, 0, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
# plt.plot(0, 1, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
# plt.plot(1, 0, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
# plt.plot(mec.center.X, mec.center.Y, marker="o", markersize=5, markeredgecolor="orange", markerfacecolor="yellow")

# plt.plot(0, 0, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
# plt.plot(0, 1, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
# plt.plot(1, 3, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
# plt.plot(4, 0, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
# plt.plot(-1, -1, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
# plt.plot(-2, 1, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
# plt.plot(-1, 3, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
# plt.plot(2, 2, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
# plt.plot([-2, 4], [1, 0], color = "blue")

ax = plt.gca()
ax.add_patch(circle)
plt.show()


# if __name__ == "__welzl_algorithm__":
#     welzl_algorithm()










