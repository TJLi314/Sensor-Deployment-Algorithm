import math
from welzl_algorithm import Point
from welzl_algorithm import dist
from kpp_algorithm import *

def get_square_point(points, d): # adds points that completes the square
    if len(points) == 0:
        # return [Point(), Point(0, d), Point(d, 0), Point(d, d)]
        return Point()
    
    poss_points = []
    # for p1 in range(len(points) - 1):
        # for p2 in range(p1 + 1, len(points)):
        #     if abs(dist(points[p1], points[p2]) - d) < 0.000000001:
        #         x1, y1, x2, y2 = points[p1].X, points[p1].Y, points[p2].X, points[p2].Y

        #         if x1 == x2:
        #             square1 = [Point(x1 + d, y1), Point(x2 + d, y2)]
        #             square2 = [Point(x1 - d, y1), Point(x2 - d, y2)]
        #         else:
        #             square1 = [Point(x1, y1 + d), Point(x2, y2 + d)]
        #             square2 = [Point(x1, y1 - d), Point(x2, y2 - d)]

        #         if not in_points(square1[0], points) and not in_points(square1[1], points):
        #             poss_points.append(square1)
        #         if not in_points(square2[0], points) and not in_points(square2[1], points):
        #             poss_points.append(square2)
    for point in points:
        x1, y1 = point.X, point.Y
        poss1, poss2, poss3, poss4 = Point(x1 + d, y1), Point(x1 - d, y1), Point(x1, y1 + d), Point(x1, y1 - d)
        if not in_points(poss1, points):
            poss_points.append(poss1)
        if not in_points(poss2, points):
            poss_points.append(poss2)
        if not in_points(poss3, points):
            poss_points.append(poss3)
        if not in_points(poss4, points):
            poss_points.append(poss4)
        
    min_width = float('inf')
    poss_point = None
    for point in poss_points:   # Return the two square points that yields the lowest width for every possible placement
        width = get_width(points + [point])[0]
        if width < min_width:
            min_width = width
            poss_point = point
    
    return poss_point
                
                



    


