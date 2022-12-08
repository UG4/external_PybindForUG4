# Import os module
import os

import sys
sys.path.append(os.environ['UG4_ROOT']+'/lib/')
print(sys.path)

import ug4py as ug4

ug4.InitUG(2, ug4.AlgebraType("CPU", 1))

dom = ug4.Domain2d()
ug4.LoadDomain(dom, "/Users/anaegel/Software/ug4-git/apps/Examples/heatsink2d/heatsink.ugx")

approxSpace = ug4.ApproximationSpace2d(dom)
approxSpace.add_fct("u","Lagrange", 1)
approxSpace.init_levels()
approxSpace.init_surfaces()
approxSpace.init_top_surface()
approxSpace.print_statistic()

dirichletBND = ug4.DirichletBoundary2d()


domainDisc = ug4.DomainDiscretization2d(approxSpace)
