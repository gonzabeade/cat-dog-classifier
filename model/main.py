import os
import sys
import train_cnn
import tensorflow as tf
import load_dataset as load
import plot as plot


if __name__ == "__main__":
    """
        Entry point for the model-generating module.

        Arguments
            - argv[1]: a path for the training data
            - argv[2]: a path for the test data
            - argv[3]: a path for a model to be loaded or created
            - argv[4]: optional - 
                a path in which to produce a sample testing image
    """
    train_ds, test_ds = load.load_dataset(sys.argv[1], sys.argv[2])
    if not os.path.exists(sys.argv[3]):
        epochs = 10
        train_cnn.new_model(train_ds, test_ds, sys.argv[3], epochs)
    model = tf.keras.models.load_model(sys.argv[3])

    if len(sys.argv) >= 4:
        plot.plot_predictions(test_ds,  sys.argv[4], 10, model)
