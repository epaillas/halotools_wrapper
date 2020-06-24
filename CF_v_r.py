from halotools.mock_observables import mean_radial_velocity_vs_r
import numpy as np

input_filename = '/home/epaillas/data/density_split/galaxy_cats/Real/\
Galaxies_HOD_001_z0.57_Real.dat'

output_filename = '/home/epaillas/data/density_split/den_cats/Real/\
Galaxies_HOD_001_z0.57_Real_HaloTools.CF_gal_v_r'

data = np.genfromtxt(input_filename)
x = data[:,0]
y = data[:,1]
z = data[:,2]

vx = data[:,3]
vy = data[:,4]
vz = data[:,5]

pos = np.c_[x, y, z]
vel = np.c_[vx, vy, vz]

bin_edges = np.linspace(0, 150, 51)
bin_centres = (bin_edges[1:] + bin_edges[:-1])/2
box_size = 1500

v_12 = mean_radial_velocity_vs_r(pos, vel, rbins_absolute=bin_edges, period=box_size)

cout = np.c_[bin_centres, v_12]

# save output
np.savetxt(output_filename, cout)