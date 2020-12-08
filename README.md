# Compositional Markov

This repository implements an algorithm for computing the most likely paths in a Markov process which occur in a fixed number of steps. This algorithm is compositional i.e. the computations it produces can be joined together to compute most likely paths on larger Markov chains. The algorithm requires that the transition matrices of your Markov process are joined in a **functional** way i.e. sinks of the first process must be joined with sources of the second process.

Transition matrices are represented by numpy arrays and are equipped with boundaries via a class `Openmat`whose use is indicated below.

```python
>>> from markov import *
>>> a = np.array([[.8,.2,.1,.72],[.25,.7,.35,.12],[0,0,0,0],[0,0,0,0]])
>>> b = np.array([[0,0,.2,.38],[0,0,.9,.92],[0,0,.21,.17],[0,0,.82,.55]])
>>> ina = [0,1]
>>> outa = [2,3]
>>> inb = [0,1]
>>> outb = [2,3]
>>> m1 = Openmat(a,ina,outa)
>>> m2 = Openmat(b,inb,outb)
```
Next the open Markov processes are precompiled to compute the most likely paths within each open Markov processes. The parameter of precompile method indicates the maximum number of steps that you are interested in computing.

```python
>>> m1.precompile(10)
>>> m2.precompile(10)
```
Open markov processes can be joined by identifing the vertices in `outa` with the vertices in `inb`.

```python
>>> compose(m1,m2)
array([[0.8 , 0.2 , 0.1 , 0.72, 0.  , 0.  ],
       [0.25, 0.7 , 0.35, 0.12, 0.  , 0.  ],
       [0.  , 0.  , 0.  , 0.  , 0.2 , 0.38],
       [0.  , 0.  , 0.  , 0.  , 0.9 , 0.92],
       [0.  , 0.  , 0.  , 0.  , 0.21, 0.17],
       [0.  , 0.  , 0.  , 0.  , 0.82, 0.55]])
```

and precompiled open matrices can be restricted to their inputs and outputs with the `blackbox()` command.

```python
>>> m1.blackbox()
array([[0.1 , 0.72],
       [0.35, 0.12]])
```
The following command computes the probabilities of the most likely paths which occur in 10 steps between the inputs of `m1` and the outputs `m2`.

```python
>>> nmostlikely(m1,m2,10)
array([[0.11391059, 0.11113228],
       [0.03559706, 0.03472884]])

```

