# Decision tree

Decision tree is a tree which nodes are kind of "tests" or "questions",
branches are outcomes and leaves are results. Decision trees can be used for
regressions and classification.

## Types

When dependent variable is discrete (__classification tree__) leaf's value is a
predicted class.

When dependent variable is continuos (__regression tree__) — leaf's value is a
predicted value. Leaf's value is calculated as a mean of all observations
ended in that leaf. This leads to a decreased accuracy.

## Attribute selection measures (or Metrics as on Wikipedia)

To build a decision tree there should be a bunch of criteria on which data will
be splitted. In general each split should make subsets more homogenous. There
are couple of algorithms to do that. The most popular is __Information Gain__ and
__Gini__.
