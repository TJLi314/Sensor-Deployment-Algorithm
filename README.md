# Sensor-Deployment-Algorithm

This algorithm will attempt to solve the k-coverage problem by deploying sensors in a circle centered at the center of a regular hexagon.

K sensors are deployed at certain points that are all separated by at least a distance of d but minimizes the distance between the two points furthest away from each other. This is done using the kpp algorithm. 

Welzl's algorithm is used to solve the minimum enclosing circle problem on the set of points to determine the radius and center of the circle in the regular hexagon to place the sensors in.

Simulations are performed to test the given sensor density for the given sensor depployment with a specific sensing radius, value k, value d, and grid size.
