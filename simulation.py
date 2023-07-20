import math
from matplotlib import pyplot as plt
from kpp_algorithm import *
from welzl_algorithm import *

def get_hexagons(sensing, radius, size):

    side = sensing - radius
    hex_height = side * math.sqrt(3)
    a_columns = math.ceil(size / hex_height)

    if hex_height * a_columns > size + (hex_height / 2):
        b_columns = a_columns
    else:
        b_columns = a_columns + 1

    num_2cols = size / (3 * side)
    num_cols = math.ceil(num_2cols * 2)

    total = 0
    for n in range(num_cols):
        if n % 2 == 0:
            total += a_columns
        else:
            total += b_columns
    
    return total

def get_density(k, sensing, radius, size):
    num = get_hexagons(sensing, radius, size)
    return k * num / (size ** 2)

def print_sensing_data(sens_vals, k_vals, d, size):
    plt.suptitle('Sensing Range vs Sensor Density', fontsize=15)
    plt.xlabel('Sensing Range (m)')
    plt.ylabel('Sensor Density (sensors/m\u00b2)')
    plt.grid()

    for k in k_vals:
        points = kpp_algorithm(k, d)
        mec = welzl_algorithm(points)
        radius = mec.radius
        
        sensing_densities = []
        for val in sens_vals:
            density = get_density(k, val, radius, size)
            sensing_densities.append(density)

        print("Changing Sensing Ranges (k = " + str(k) + "): ", sensing_densities)

        label = "k = " + str(k)
        plt.plot(sens_vals, sensing_densities, label=label, linewidth = 2)
    
    plt.legend()
    plt.show()

def print_k_data(k_vals, sensing, d, size):
    plt.suptitle('K-value vs Sensor Density', fontsize=15)
    plt.xlabel('K-values')
    plt.ylabel('Sensor Density (sensors/m\u00b2)')
    plt.grid()

    sensing_densities = []
    for k in k_vals:
        points = kpp_algorithm(k, d)
        mec = welzl_algorithm(points)
        radius = mec.radius
        
        density = get_density(k, sensing, radius, size)
        sensing_densities.append(density)

    print("Changing K-values: ", sensing_densities)

    print
    plt.plot(k_vals, sensing_densities, linewidth = 2)
    
    plt.show()

def print_d_data(d_vals, k_vals, sensing, size):
    plt.suptitle('Minimum Distance Between Sensors vs Sensor Density', fontsize=15)
    plt.xlabel('Distance (m)')
    plt.ylabel('Sensor Density (sensors/m\u00b2)')
    plt.grid()

    for k in k_vals:
        sensing_densities = []
        for d in d_vals:
            points = kpp_algorithm(k, d)
            mec = welzl_algorithm(points)
            radius = mec.radius
    
            density = get_density(k, sensing, radius, size)
            sensing_densities.append(density)

        print("Changing d (k = " + str(k) + "): ", sensing_densities)

        label = "k = " + str(k)
        plt.plot(d_vals, sensing_densities, label=label, linewidth = 2)
    
    plt.legend()
    plt.show()

def print_radius_data(d_vals, k_vals):
    plt.suptitle('Minimum Distance Between Sensors vs Radius', fontsize=15)
    plt.xlabel('Distance (m)')
    plt.ylabel('Radius (m)')
    plt.grid()

    for k in k_vals:
        radi = []
        for d in d_vals:
            points = kpp_algorithm(k, d)
            mec = welzl_algorithm(points)
            radius = mec.radius
    
            radi.append(radius)

        print("Changing d for radius (k = " + str(k) + "): ", radi)

        label = "k = " + str(k)
        plt.plot(d_vals, radi, label=label, linewidth = 2)
    
    plt.legend()
    plt.show()

def print_connectivity(d_vals, k, sensing):
    plt.suptitle('Minimum Distance Between Sensors vs Connectivity', fontsize=15)
    plt.xlabel('Distance (m)')
    plt.ylabel('Connectivity Radius (m)')
    plt.grid()

    
    connectivities = []
    for d in d_vals:
        points = kpp_algorithm(k, d)
        mec = welzl_algorithm(points)
        radius = mec.radius
        connectivity = math.sqrt(3) * (sensing - radius) + 2 * radius

        connectivities.append(connectivity)

        print("Changing d for radius (k = " + str(k) + "): ", connectivities)

        
    plt.plot(d_vals, connectivities, linewidth = 2)
    plt.show()
    



    

