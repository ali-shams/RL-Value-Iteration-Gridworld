# Rl - Grid World Value Iteration

---
This project involves creating a grid world environment and applying value iteration to find the optimum policy. Below is the value iteration pseudocode that was programmed and tested [[1]](#1).
![Alt text](images/Value_iteration_pseudocode.png?raw=true "Optional Title")
The state space of the grid world was represented using a dynamic NumPy array with the index system as shown below.
![Alt text](images/Grid_instances.png?raw=true "Optional Title")
For the stochastic environment, there is a dynamic probability that the agents move as intended. Below shows the values and policies derived from this stochastic environment. The simulation parameters are defined as follows:
$$\gamma=1, \theta=1^{-10}, p(s^{'},r|s,a)=0.7, volcano\_penalty=-10, goal\_reward=10$$
![Alt text](images/Values_and_policies.png?raw=true "Optional Title")

---
## References
<a id="1">[1]</a>  R. S. Sutton and A. G. Barto, Reinforcement Learning: An Introduction, 2nd ed., Cambridge, England, The MIT Press, 2018.

