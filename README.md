# SysAnalysisLabs
Python scrips that were made during system analysis course

simplex.py is a Python script that solves linear programming task with simplex method.
  It has an output into simplex.txt file to research parameters at every step.
  
dynamicProg.py - script that solves dynamic programming task of minimal cost. 
Example: given two arrays R and C that defines costs of travelling throught rows ans columns of graph.
Scripts computes whole graph and search for a path. As it was found, script generates HTML file where displayed graph and path elements that highlighted in red.

gradientMethod.py - script for finding a local minimum of a defferentiable function using gradient descent. 
As input script gets: the function under study and derivatives with respect to its arguments, initial point and axis boundaries.
1) Script visualize function in given boundaries. 
2) It computes gradient of function at initial point.
3) Computes new point - a point after offset with given step and gradient value.
4) Function values at two points are compared, and if value at the new point is less than in old one, script executed further. Otherwise, step divides in half and Step 3 repeats.
5) Accuracy check: if the difference in the coordinates of two points is less than given accuracy (0.01 by default), then script repeats from Step 2, otherwise computation is over.

The values of following parameters are written in gradient.txt file throughout the calculation: Iteration, starting point, new point, func value at the starting point, func value at the new point,  function gradient at the starting point, function gradient at the new point, accuracy.
