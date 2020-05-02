# k-nearest neighbors (k-NN, KNN)

It's a non-parametric* method commonly used for classification and
regression problems.

On input there are __k__ nearest** neighbors (or more scientifically
— training example in the feature space). Output differs depending on
a problem type:

- for classification it outputs the most common (mode) class among
neighbors.
- for regression it outputs average of neighbors' values.

* Non-parametric means that method does not rely on any type of distribution AFAIK.

** Distance can be measured by several different ways. The simplest
method for continuous variables is Euclidean distance. For discrete
variables choice depends on specific data.
