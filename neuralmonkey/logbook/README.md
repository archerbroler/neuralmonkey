# Neural Monkey LogBook

## What is it?

_Neural Monkey LogBook_ is a simple web application for preview the outputs of
the experiments in the browser.

The experiment data are stored in a directory structure where each experiment
directory contains the experiment configuration, state of the git repository,
the experiment was executed with, detailed log of the computation and other
files necessary to execute the model that has been trained.

LogBook is meant as a complement to using
[TensorBoard](https://www.tensorflow.org/versions/r0.9/how_tos/summaries_and_tensorboard/index.html)
whose summaries are stored in the same directory structure.

## How to run it?

You can run the server using the following command:

`python neuralmonkey/logbook/logbook.py --logdir=<experiments> --port=<port>`

where `<experiments>` is the directory where the experiments are listed and
`<port>` is the number of the port the server will run on.

Then you can navigate in your browser to `http://localhost:<port>` to view the
experiment logs.
