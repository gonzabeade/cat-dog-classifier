# Cat-Dog Classifier

This project implements an end-to-end system for classifying pictures containing cats or dogs. 

However simple the deep learning model may be, the intention of this project is to integrate it in a bigger architecture and deploy it as a fully functional full-stack application. 

### Structure
The repository consists of three modules. More information about each module can be obtained in their respective `README` files. 
1. `/model` contains the source files for constructing, training and exporting a convolutional neural network using Keras. 
2. `/client` contains the source files for the frontend of the project, a React-based single-page application. A user can upload a picture and wait for a prediction to be displayed. 
3. `/server` contains the source files for the backend of the project. The server exposes endpoints for uploading a picture and querying its predicted value, following REST guidelines. 


