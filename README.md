# Spring-Mass-Dynamics
A Simulation of Spring Mass Dynamics

## About the Simulation
This simulation uses the finite difference and Gauss Seidel methods to compute forward
to arbitrary timesteps

![spring mass](img/animation.gif)

The intial conditions of the sytem are as follows:

initial displacement was `x = 0.7 m` from rest. The mass of the weight was `m = 2.0 kg`.
The restoring force from the initial displacement was `N = 25.6 N`. the spring constant
`k` was calculated with [Hooke's Law](https://en.wikipedia.org/wiki/Hooke%27s_law): giving `k = -1 * (N/x)`

The finite difference method converts the following equation into its descrete form:

![Equation 1](img/EQ1.gif)


## Dependencies
* python2.7
* matplotlib
* numpy

## Running

To see the animated simulation, simply run: `python simulation.py`
