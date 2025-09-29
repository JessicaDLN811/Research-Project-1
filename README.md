# Research-Project-1
Root-Finding Methods Visualization in Python

A Python project implementing and comparing four numerical root-finding methods: Bisection, Newton-Raphson, Secant, and Muller. This project demonstrates the iterative process of approximating roots for nonlinear equations and visualizes error convergence to highlight efficiency differences between methods.

Features

Implements four classic root-finding algorithms from scratch using Python.

Displays iteration tables showing approximations and errors at each step.

Provides visual plots of error convergence for a clear comparison of method efficiency.

design allows for easy testing with any differentiable function.

Methods Implemented

Bisection Method – A robust bracketing method.

Newton Method – Uses derivatives for faster convergence.

Secant Method – Approximates derivative for iterative convergence.

Muller Method – Handles complex roots and uses quadratic interpolation.

Example Usage
python root_methods.py

The script will:

Compute roots of the following functions:

f1(x) = x^3 - 5x^2 + 2x

f2(x) = x^3 - 2x^2 - 5

Print tables of iterations with errors.

Display log-scale plots of error convergence for each method.

Sample Table Output
Newton f1 Method
Iter | x_n        | Error
-------------------------------
   0 | 0.500000   |    -
   1 | 0.414216   | 8.585420e-02
   2 | 0.387281   | 2.696600e-02
...
Final Approx: 0.382333

Dependencies

Python 3.x

numpy

matplotlib

Install dependencies via pip:

pip install numpy matplotlib

Why This Project

This project is designed to showcase:

Proficiency in Python and numerical methods.

Analytical and visualization skills in comparing algorithms.

Ability to write clean, modular, and reusable code.

Apt for recruiters in software engineering, data science, and computational fields.

Future Enhancements

Add support for user-defined functions via CLI or GUI.

Compare performance metrics (speed, iterations) across methods.

Extend visualization for complex roots handling in Muller method
