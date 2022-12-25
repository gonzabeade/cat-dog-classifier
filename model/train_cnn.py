from keras.models import Sequential
from load_dataset import load_dataset
from keras.layers import Conv2D, MaxPooling2D, Flatten, \
                            Dense, Rescaling, Resizing


def new_model(train_ds, test_ds, model_path, epochs):
    """
        Given the path to a training set, a path where to 
        save the model and a quantity of epochs, the method
        generates and saves a convolutional neural network.

        Input:
            - a train directory path
            - a path where to save the trained model
            - a number of epochs

        Output: None, but saves a model as a secondary effect
    """

    # Rescaling layer
    # - Normalize RGB values so that they are between 0 and 1
    layer_rescale = Rescaling(1./255, name='l_rescaling')

    # Resizing layer
    # - Crop the image so that it is of size 64 by 64
    layer_resize = Resizing(64, 64, crop_to_aspect_ratio=True, name='l_resize')

    # Convolutional layer
    # - 32 filters in total
    # - 3x3 shape of each filter
    # - Each input will be RGB and 64x64
    # - ReLU as an activation function
    layer_1 = Conv2D(
        32, 
        (3, 3),
        input_shape=(64, 64, 3),
        activation='relu', 
        name='l_conv'
    )

    # Pooling layer
    # - We will use MaxPooling
    # - The pool size is 2x2
    layer_2 = MaxPooling2D(pool_size=(2, 2), name="l_pool")

    # Flattening later
    layer_3 = Flatten(name="l_flatten")

    # Fully connected layer
    # - 128 neurons
    # - ReLU as an activation function
    layer_4 = Dense(
        units=128, 
        activation='relu',
        name='l_dense'
    )

    # Output layer
    # - Sigmoid as an activation
    layer_output = Dense(
        units=1, 
        activation='sigmoid', 
        name='l_output'
    )

    # Build the model
    layers = [
        layer_resize,
        layer_rescale,
        layer_1, 
        layer_2, 
        layer_3, 
        layer_4, 
        layer_output
    ]
    classifier = Sequential()
    for layer in layers:
        classifier.add(layer)

    classifier.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    # Train the model
    classifier.fit(train_ds, epochs=epochs)

    # Test the model
    classifier.evaluate(test_ds)

    # Save the model
    classifier.save(model_path)
