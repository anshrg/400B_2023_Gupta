import numpy as np
from astropy import units as u
from ReadFile import Read

def ComponentMass(filename, particle_type):
    '''
    This function returns the total mass of a given galaxy component (particle type)
    
    Inputs:
        filename: 'string'
                Name of the datafile of the galaxy to be analyzed
    
        particle_type: 'int'
                Galaxy component to be analyzed. Number from 1-3
                1 = Halo, 2 = Disk, 3 = Bulge
      
    Outputs:
        mass: 'float'
                Mass of the desired galaxy component (10^12 M_Sun, 3 decimal places)
    '''
    
    _, _, data = Read(filename) # Read in data array from datafile
    type_index = np.where(data['type'] == particle_type) # Indices of particles of given type
    particles_of_type = data[type_index]['m'] # Get masses of particles within component
    mass = np.sum(particles_of_type) * 1e10 * u.M_sun # Sum particle masses with units
    return np.round(mass / 1e12, 3) # Return mass in desired units with rounding