# NIPS Assignments

This directory contains code that was used by the NIPS 2017 program chairs,
mosty to help them assign papers to reviewers and area chairs, as well as
assign area chairs to senior area chairs.
NIPS is the main machine learning conference (www.nips.cc).
The program chairs for 2017 were Samy Bengio, Hanna Wallach, Rob Fergus and
S.V.N. Vishwanathan.

NIPS usually use CMT (cmt.research.microsoft.com) to handle the reviewing
process, and the program chairs could have use it as well for the assignment
tasks, but they felt the need to control more precisely the assignments,
for instance by better balancing the interests of the reviewers and the area
chairs, and adding various constraints for fairness (such as the number of
reviewers from the same organization for a given paper).

In order to use this code, you first need to install the Google operations
research toolbox, details here:
https://developers.google.com/optimization/introduction/installing
Once this is done, modify OR_DIR in Makefile to point
to the underlying or-tools directory, then run "make".

Furthermore, it is recommended to install additional third-party solvers
such as SCIP and GUROBI to obtain a faster result, in particular for the
large assignment problem between reviewers and papers. Details about
installing them are available on the Google operations research toolbox
installation page.

Note that this is not an official Google product.

Samy Bengio

Google Brain
