import matplotlib.pyplot as plt


def plot_dataset(ds, path, many):
    """
        Plots a random sample of the pictures in a dataset and saves it
        to a file

        Input:
            - a Dataset instance
            - a path for the plot is to be saved
            - the number of samples in the plot
    """

    # Get the class names from the dataset
    class_names = ds.class_names

    # Set the dimension of the figure
    plt.figure(figsize=(15, 15))

    # Take a batch from the dataset
    for images, labels in ds.take(1):
        for i in range(many):
            plt.subplot(int(many/3)+1, 3, i+1)
            plt.imshow(images[i].numpy().astype("uint8"))
            plt.title(class_names[labels[i]])
            plt.axis("off")
    plt.savefig(path)


def plot_predictions(ds, path, many, model):
    """
        Plots a random sample of the pictures in a dataset.
        For each sample, the actual and predicted labels are shown.

        Input:
            - a Dataset instance
            - a path where the plot is to be saved
            - the number of samples in the plot
            - a classifier model
    """

    # Get the class names from the dataset
    class_names = ds.class_names

    # Set the dimension of the figure
    plt.figure(figsize=(15, 15))

    # Take a batch from the dataset
    for images, labels in ds.take(1):
        for i in range(many):
            plt.subplot(int(many/3)+1, 3, i+1)
            im = images[i].numpy().astype("uint8")
            plt.imshow(im)

            im = im.reshape(1, im.shape[0], im.shape[1], im.shape[2])
            result = model.predict(im)
            result = 0 if result[0][0] < 0.5 else 1

            plt.title(
                "{} - Predicted: {}"
                .format(
                    class_names[labels[i]],
                    class_names[result]
                )
            )
            plt.axis("off")
    plt.savefig(path)
