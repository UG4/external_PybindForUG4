# external_PybindForUG4

Third party tools for pybind11. Consult license in subdirectory for details.

This part is experimental! To install this software:

1) Install via ughub. This will create ``externals/PybindForUG4``

```
cd $UG4_ROOT
ughub install PybindForUG4
```

2) The next step is to fetch and to update the submodules:

```
ughub git submodule init --- PybindForUG4
ughub git submodule update --- PybindForUG4 
```
Note that specifying ``--- PybindForUG4`` is optional.

3) Now you have external libraries installed. Configure UG4 with CMakeFlags '-DUSE_PYBIND11=ON' and recompile:

```
cmake -DUSE_PYBIND11=ON -DCMAKE_POLICY_DEFAULT_CMP0057=NEW
```
(Note: Setting the policy is only required on newer cmake versions).

4) Finally, you can execute a small demo as follows:
```
cd $UG4_ROOT/externals/PybindForUG4
python3 src/ug4demo.py
```

