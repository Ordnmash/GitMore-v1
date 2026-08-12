# GitMore-v1
## Gitmore v1 is the NN model built on ANN - MLP, with the dataset of git commits messages.
the dataset is collected from the Cpython open source code to train the model to generate the Git commits learned from data.
the length of the dataset is roughly 180k of commits strings

<p align="center">
  <img src="gitmore_logo.png" width="800" height="400" alt="tictactoe_Robot">
</p>

### The model size is `265k parameters` with `13 layers` |  input size of `vocab_size by n_embd`  |  output size of  `n_hidden by vocab_size`
<hr>
### this was a very successful training with a very good training and validation loss out of the model!
before training, the model had an `initialization loss of 4.642845` which is few inches about the `projected initial loss of 4.5539`
<hr>
after 500k epochs I got a very good surprising `validation loss of around 1.516756` with `training loss of 1.301701` 
this yield to very good commits messages when sampling.
