# Compositional Markov

This repository implements an algorithm for computing the most likely paths in a Markov process which occur in a fixed number of steps. This algorithm is compositional i.e. the computations it produces can be joined together to compute most likely paths on larger Markov chains. It requires that the transition matrices of your Markov process are joined in a **functional** way i.e. sinks of the first process must be joined with sources of the second process.





