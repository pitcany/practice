#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 13:58:37 2019

@author: yannik
"""

 from __future__ import print_function
 from ortools.linear_solver import pywraplp
 
 def main():
     solver = pywraplp.Solver('LinearExample',
                              pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
     # Create the variables x and y.
     x = solver.NumVar(-solver.infinity(), solver.infinity(), 'x')
     y = solver.NumVar(-solver.infinity(), solver.infinity(), 'y')
     # Constraint 1: x+2y <= 14.
     constraint1 = solver.Constraint(-solver.infinity(), 14)
     constraint1.SetCoefficient(x, 1)
     constraint1.SetCoefficient(y, 2)
     # Constraint 2: 3x - y >= 0.
     constraint2 = solver.Constraint(0, solver.infinity())
     constraint2.SetCoefficient(x, 3)
     constraint2.SetCoefficient(y, -1)
     # Constraint 3: x - y <= 2.
     constraint2 = solver.Constraint(-solver.infinity(), 2)
     constraint2.SetCoefficient(x, 1)
     constraint2.SetCoefficient(y, -1)
     # Create the objective function, 3x+4y.
     objective = solver.Objective()
     objective.SetCoefficient(x, 3)
     objective.SetCoefficient(y, 4)
     objective.SetMaximization()
     # Call the solver and display the results
     solver.Solve()
     opt_solution = 3*x.solution_value() + 4*y.solution_value()
     print('Number of variables =', solver.NumVariables())
     print('Number of constraints =', solver.NumConstraints())
     # The value of each variable in the solution
     print('Solution:')
     print('x = ', x.solution_value())
     print('y = ', y.solution_value())
     # The objective value of the solution.
     print('Optimal objective value =', opt_solution)
 
 if __name__ == '__main__':
     main()