# Import os module
import os
env_ug4_root = os.environ['UG4_ROOT']

import sys
sys.path.append(env_ug4_root+'/lib/')
print(sys.path)

import ug4py as ug4

ug4.InitUG(2, ug4.AlgebraType("CPU", 1))

dom = ug4.Domain2d()
ug4.LoadDomain(dom, env_ug4_root + "/apps/Examples/heatsink2d/heatsink.ugx")

approxSpace = ug4.ApproximationSpace2d(dom)
approxSpace.add_fct("u","Lagrange", 1)
approxSpace.init_levels()
approxSpace.init_surfaces()
approxSpace.init_top_surface()
approxSpace.print_statistic()

dirichletBND = ug4.DirichletBoundary2d()


domainDisc = ug4.DomainDiscretization2d(approxSpace)
