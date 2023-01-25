# This function reads a datafile and returns the snapshot time, number of particles, and a data array
# Inputs: filename (name of file to be read, string)
# Returns: time (SnapNumber*10/0.7 in Myr), number_of_particles (int), data (type, mass, position, velocity for each particle, numpy array)

import numpy as np
import astropy.units as u

def Read(filename):
    with open(filename, 'r') as file: # open data file using context manager
        line1 = file.readline() # read line 1
        line2 = file.readline() # read line 2

    label, value = line1.split() # unpack first line
    time = float(value)*u.Myr # time value from first line with units of Myr
    label, value = line2.split() # unpack second line
    number_of_particles = int(value) # get number of particles from second line

    # convert line 4 onwards to an array of attributes for each particle,
    data = np.genfromtxt(filename, dtype=None, delimiter=None, names=True, skip_header=3) 
    return time, number_of_particles, data
