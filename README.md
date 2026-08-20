# GitMore-v1
## Gitmore v1 is the NN model built on ANN - MLP, with the dataset of git commits messages.
the dataset is collected from the Cpython open source code to train the model to generate the Git commits learned from data.
the length of the dataset is roughly 180k of commits strings
<p align="center">
  <img src="gitmore_logo.png" width="800" height="400" alt="GitMore_logo">
</p>

### The model size is `265k parameters` with `13 layers`
<hr>
this was a very successful training with a very good training and validation loss out of the model!
before training, the model had an `initialization loss of 4.642845` which is few inches about the `projected initial loss of 4.5539`
<hr>
after 500k epochs I got a very good surprising <b>validation loss of around <span style="color📘;"><i>1.516756</i></span></b> with <b>training loss of <i>1.301701</i></b> 
this yield to very good commits messages when sampling.
