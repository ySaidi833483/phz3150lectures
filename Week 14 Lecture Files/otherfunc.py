import numpy as np

def circle_a_and_v(R = None):
    """ Returns the surface area and volume of a sphere of radius R as a tuple.
    """
    if R is None:
        print("no radius given!")
        return None 
    else:
        return np.pi*4*R**2