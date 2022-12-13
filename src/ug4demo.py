# Import os module
import os
env_ug4_root = os.environ['UG4_ROOT']

import sys
sys.path.append(env_ug4_root+'/lib/')
sys.path.append(env_ug4_root+'/bin/plugins/ug4py')
print(sys.path)

import ug4py as ug4
import pylimex as limex
import pyconvectiondiffusion as cd


# Initialize UG4
ug4.InitUG(2, ug4.AlgebraType("CPU", 1))

# Load domain.
dom = ug4.Domain2d()
ug4.LoadDomain(dom, env_ug4_root + "/apps/Examples/grids/laplace_sample_grid_2d.ugx")

# Create approximation space.
approxSpace = ug4.ApproximationSpace2d(dom)
approxSpace.add_fct("u","Lagrange", 1)
approxSpace.init_levels()
approxSpace.init_surfaces()
approxSpace.init_top_surface()
approxSpace.print_statistic()


# Create discretization.
elemDisc = cd.ConvectionDiffusionFV12d("u", "INNER")

# dirichletBND = ug4.DirichletBoundary2d()

domainDisc = ug4.DomainDiscretization2dCPU1(approxSpace)
domainDisc.add(elemDisc)

nstages = 2
limex = limex.LimexTimeIntegrator2dCPU1(nstages)

