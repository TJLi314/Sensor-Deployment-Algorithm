from simulation import *

def main():
        
        sens_vals = [20, 25, 30, 35, 40, 45, 50]
        k_vals = [2, 3, 4, 5, 6, 7, 8]
        print_sensing_data(sens_vals, k_vals, 2, 500)

        print_k_data([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 25, 2, 500)

        d_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print_d_data(d_vals, k_vals, 25, 500)

        print_radius_data(d_vals, k_vals)

        print_connectivity(d_vals, 4, 25)

        
if __name__ == "__main__":
        main()

