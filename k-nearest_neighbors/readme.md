# k-nearest neighbors (k-NN, KNN)

## Description

It's a non-parametric[¹] method commonly used for classification and
regression problems.

On input there are __k__ nearest[²] neighbors (or more scientifically
— training examples in the feature space). Output differs depending on
a problem type:

- for classification it outputs the most common (mode) class among
neighbors.
- for regression it outputs average of neighbors' values.


#### [¹] Non-parametric means that method does not rely on any type of distribution AFAIK.
[¹]:#-note-one

#### [²] Distance can be measured by several different ways. The simplest method for continuous variables is Euclidean distance. For discrete variables choice depends on specific data.
[²]:#-note-one

## Instructions

Generate dataset

```
$ ruby generate_dataset.rb
```

Run prediction code

```
$ python knn.py
```
