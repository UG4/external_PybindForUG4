# Import os module
#import time
#time.sleep(30) # for debugging

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
ug4.LoadDomain(dom, "skin2d-aniso.ugx")

# Create approximation space.
approxSpace = ug4.ApproximationSpace2d(dom)
approxSpace.add_fct("u","Lagrange", 1)
approxSpace.init_levels()
approxSpace.init_surfaces()
approxSpace.init_top_surface()
approxSpace.print_statistic()


# Create discretization.
KDcor=1.0
KCor=1.0

elemDiscCor = cd.ConvectionDiffusionFV12d("u", "COR")
elemDiscCor.set_diffusion(KDcor)
elemDiscCor.set_mass_scale(KCor)

elemDiscLip = cd.ConvectionDiffusionFV12d("u", "LIP")
elemDiscLip.set_diffusion(KDcor)
elemDiscLip.set_mass_scale(KCor)

dirichletBND = ug4.DirichletBoundary2dCPU1()
dirichletBND.add(1.0, "u", "TOP_SC")
dirichletBND.add(0.0, "u", "BOTTOM_SC")

domainDisc = ug4.DomainDiscretization2dCPU1(approxSpace)
domainDisc.add(elemDiscCor)
domainDisc.add(elemDiscLip)
domainDisc.add(dirichletBND)



ilu=ug4.ILUCPU1()
lsolver=ug4.LinearSolverCPU1()
lsolver.set_preconditioner(ilu)

# lsolver=ug4.LUCPU1()


usol = ug4.GridFunction2dCPU1(approxSpace)
ug4.Interpolate(0.0, usol, "u")

startTime = 0.0
endTime = 10.0
dt=0.25

print(issubclass(ug4.LUCPU1,ug4.ILinearOperatorInverseCPU1))
print(isinstance(lsolver,ug4.LUCPU1))
print(isinstance(lsolver,ug4.ILinearOperatorInverseCPU1))

print(lsolver)
print(lsolver.__class__)
print(lsolver.name())
print(lsolver.config_string())
print(super(ug4.LUCPU1))

timeDisc=ug4.ThetaTimeStepCPU1(domainDisc, 1.0)

timeInt = limex.LinearTimeIntegrator2dCPU1(timeDisc)
#timeInt = limex.ConstStepLinearTimeIntegrator2dCPU1(timeDisc)
timeInt.set_linear_solver(lsolver)
timeInt.set_time_step(dt)

try:
    timeInt.apply(usol, endTime, usol, startTime)
except Exception as inst:
    print(type(inst))    # the exception instance
   # print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    


# nstages = 2
# limex = limex.LimexTimeIntegrator2dCPU1(nstages)

