import tensorflow as tf


def load_dataset(path_train, path_test):
    """
        Given the paths to train and test directories,
        the method returns a tuple of two Dataset instances.
        Notice subdirectory must have its samples separatd in
        correctly-labeled folders.

        Input:
            - a train directory path
            - a test directory path

        Output: a tuple of train and test Dataset instances
    """
    train_ds = tf.keras.utils.image_dataset_from_directory(path_train)
    test_ds = tf.keras.utils.image_dataset_from_directory(path_test)
    return train_ds, test_ds
