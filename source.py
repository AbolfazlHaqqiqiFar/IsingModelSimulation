# We define the main function in which the code is executed


from medium import Medium
import matplotlib.pyplot as plt
import numpy as np

def main():
    for i in np.arange(0, 0.5, 0.01):
        medium = Medium(num = 64, dim = 1, initial_config="stochastic",\
            initial_direction= -1, J=1, steps = 1000, temp = i )

        aveE , aveP = medium.Evolution(display=False)
        print("%-5.3f %-5.3f %-5.3f" %(i, aveE, aveP))
        medium.WriteTheLattice()
        print("#", "-"*70)
        
    
main()