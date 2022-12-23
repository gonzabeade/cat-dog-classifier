## Model: CNN

This repository contains the necessary files to successfully train a CNN to identify whether a picture contains cats or dogs. 

### Installation 

#### 1. Virtual Environment
It is highly recommended - yet optional - to create a virtual environment before executing this project. This can be done simply by running 

`python3 -m venv .venv`

The file `requirements.txt` contains all dependencies. These can be installed with 

`pip install -r requirements.txt`

#### 2. Setup

The directories which contain the training and test data have to be correctly structured for the project to run. Both the training and test data directories must contain two folders `cat` and `dog`, each containing the appropriate images. 

The network may receive as input RGB pictures of any size. The following [dataset](https://www.kaggle.com/datasets/tongpython/cat-and-dog) was used to train the network. 

#### 3. Initialization

The entry point for the module is `main.py`. It receives three compulsory parameters and a fourth optional parameters. 
1. A path to the training dataset, structured as previously described. 
2. A path to the test dataset, structured as previously described. 
3. An output path, where the generated model is to be saved. If the model already exists, it is simply loaded. 
4. Optional. A path for a simple digest plot of the predictions to be dumped. 

#### 3. CNN Architecture

The module generates a trained convolutional neural network. The sequential model is made up of the following layers: 
1. A resizing layer, so that any picture has size 64x64 before being input to the CNN. 
2. A rescaling layer, for normalizing RGB values between 0 and 1. 
3. A convolutional layer with 32 3x3 filters and ReLU activation function. 
4. A pooling layer, using max-pool and a pool size of 2x2. 
5. A flattening layer. 
6. A fully-connected layer of 128 nodes and ReLU activation function. 
7. An output node with sigmoid activation function. 

ADAM was used as an optimizer and binary cross-entropy as a loss function. 

#### 4. Output

The module exports a trained model with the previously described architecture and 10 epochs by default. Optionally, if a path is specified as fourth argument, a sample of pictures is taken from the test set and a digest plot is exported. 





