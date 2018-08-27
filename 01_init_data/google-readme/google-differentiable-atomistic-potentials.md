#+TITLE: Differentiable atomistic potentials
#+AUTHOR: John Kitchin

This is not an official Google product.
#+BEGIN_EXPORT html
<a href='https://travis-ci.org/google/differentiable-atomistic-potentials'><img src='https://travis-ci.org/google/differentiable-atomistic-potentials.svg?branch=master'/></a>
<a href='https://coveralls.io/github/google/differentiable-atomistic-potentials?branch=master'><img src='https://coveralls.io/repos/github/google/differentiable-atomistic-potentials/badge.svg?branch=master' alt='Coverage Status' /></a>
#+END_EXPORT


* Summary

An atomistic potential is a function that takes atomic coordinates, atom types and a unit cell and calculates the potential energy of that atomic configuration. These potentials are used in molecular simulations such as molecular dynamics and Monte Carlo Simulations. Historically, the forces and stress were derived by analytical or numerical derivatives of the potential energy function, then implemented in a program. In this project, we use automatic differentiation to compute forces and stresses from the potential energy program. This project focuses on materials that are described by periodic boundary conditions.

The first demonstration of this approach is for the Lennard Jones potential, which is fully implemented in TensorFlow to compute energies, forces and stress of periodic atomic systems containing one kind of chemical element. The potential is trainable from a database of reference data, e.g. density functional theory calculations. An example is illustrated in [[./docs/dap.tf.lennardjones.org]].

* Installation

If you have root access, and you want to install the bleeding edge version system-wide, it should be sufficient to run:

#+BEGIN_SRC sh
pip install git+git://github.com/google/differentiable-atomistic-potentials
#+END_SRC

If you want an editable, developer installation you might prefer this:

#+BEGIN_SRC sh
git clone https://github.com/google/differentiable-atomistic-potentials.git
cd differentiable-atomistic-potentials
pip install --user -e .
#+END_SRC

* Related projects
  
The earliest code we are aware of is [[http://www.theochem.ruhr-uni-bochum.de/~joerg.behler/runner.htm][Runner]], but it is only available by request from the authors.

- [[https://bitbucket.org/andrewpeterson/amp][Amp]] cite:khorshidi-2016-amp is an open-source Python/Fortran package for machine learned neural network potentials.
- [[https://biklooost.github.io/PROPhet/][PROPhet]] cite:kolb-2017-discov-charg is an open-source package for machine learned neural network potentials.
- [[http://ann.atomistic.net/Documentation/][aenet]] cite:artrith-2016 is an open source Fortran package for machine learned neural network potentials.

This project is complementary to those projects. We share a common goal of open-source machine learned neural network potentials. Our approach differs primarily in the use of automatic differentiation to enable efficient training as well as automatic forces and stresses. We also aim to make it possible to generate hybrid potentials comprised of a classical potential and a neural network potential.

- TensorMol https://github.com/jparkhill/TensorMol is an open source package focused on molecular properties. It also uses TensorFlow.

- DiffiQult https://github.com/aspuru-guzik-group/DiffiQult  (https://arxiv.org/abs/1711.08127) is an open source autodifferentiable quantum chemistry package.

- DeePMD https://arxiv.org/abs/1707.09571 Deep Potential Molecular Dynamics: a scalable model with the accuracy of quantum mechanics
   
** Automatic differentiation toolkits

Here are a few of the AD toolkits that are currently around. 
   
- [[https://github.com/HIPS/autograd][autograd]] :: A Numpy/Python framework
- [[https://www.tensorflow.org/][Tensorflow]] :: An open-source machine learning framework for everyone
- [[https://github.com/google/tangent][tangent]] :: Source-to-Source Debuggable Derivatives in Pure Python

I have not tried these
- [[https://pypi.python.org/pypi/algopy][algopy]] ::  a tool for Algorithmic Differentiation (AD) and Taylor polynomial approximations.
- pytorch :: Another machine learning framework in Python
- Chainer :: Another machine learning framework in Python
	     
* Roadmap

These projects are planned in the future.
- [X] Vectorized neighborlists for periodic boundary conditions [[./dap/ag/neighborlist.py][autograd]] and [[./dap/tf/neighborlist.py][TensorFlow]].
- [X] Vectorized one-way neighborlists for periodic boundary conditions [[./dap/ag/neighborlist.py][autograd]] and Tensorflow
- [X] Lennard Jones potential in [[./dap/ag/lennardjones.py][autograd]] and [[./dap/tf/lennardjones.py][Tensorflow]].
- [ ] Effective medium theory for multicomponent alloys in [[./dap/ag/emt.py][autograd]] and Tensorflow
- [ ] Behler-Parinello Neural Network for multicomponent systems

* Requirements

This project is written for Python 3.6.

See [[./requirements.txt]] for a list of required Python packages.

