from matplotlib import pyplot as plt
from kpp_algorithm import *
from welzl_algorithm import *


def main():
        
        plt.gca().set_aspect("equal")
        plt.axis([-1.5, 2.5, -2, 2])
        

        points = kpp_algorithm(7, 1)
        print_points(points)

        mec = welzl_algorithm(points)
        print("Center = {",mec.center.X,",",mec.center.Y,"} Radius =",mec.radius)

        # plt.plot(mec.center.X, mec.center.Y, marker="o", markersize=5, markeredgecolor="pink", markerfacecolor="blue")
        circle = plt.Circle((mec.center.X, mec.center.Y), mec.radius, fill = False, edgecolor = "blue", linewidth = 5)

        ax = plt.gca()
        ax.add_patch(circle)
        plt.show()

if __name__ == "__main__":
        main()

