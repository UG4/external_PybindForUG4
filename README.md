# external_PybindForUG4

Third party tools for pybind11. Consult license in subdirectory for details.

This part is experimental! To install this software:

1) Install via ughub. This creates externals/PybindForUG4

2) Go to ``externals/PybindForUG4``. Install via:

```
git submodule init
git submodule update
```

3) Now you have external libraries installed. Configure UG4 with CMakeFlags '-DUSE_PYBIND11=ON' and recompile:

```
cmake -DUSE_PYBIND11=ON -DCMAKE_POLICY_DEFAULT_CMP0057=NEW
```
(Note: Setting the policy is only required on newer cmake versions).

