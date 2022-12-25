from fastapi import FastAPI, Header, Depends, \
     HTTPException, status, File, UploadFile
import uvicorn
import sys
import tensorflow as tf
from PIL import Image
import io 
import numpy as np 
from matplotlib import pyplot as plt 


# Uninstall flake8

app = FastAPI()
model = None
valid_image_types = ["png", "jpeg", "jpg"]


def val_content_type(file: UploadFile):
    """
        Validates the request content-type to be image/png
    """
    type = file.content_type.split("/")
    print(type[1], type[1] not in valid_image_types)
    if type[0] != "image" or type[1] not in valid_image_types:
        raise HTTPException(
            status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            f"Unsupported media type: {file.content_type}."
        )


@app.post("/images")
async def images(
    file: UploadFile = File(...)
):
    # val_content_type(file)

    bytes = await file.read()
    im =  np.asarray(Image.open(io.BytesIO(bytes))).astype("uint8")
    print(im.shape)
    plt.imshow(im)
    im = np.expand_dims(im, axis=0)
    print(im.shape)
    print(model.predict(im))
    await file.close()       
    return {"message": file.content_type}


if __name__ == '__main__':
    """
        Entry point for the backend module.

        Arguments
            - argv[1]: host
            - argv[2]: port
            - argv[3]: path from where to load a trained model
    """
    model = tf.keras.models.load_model(sys.argv[3])
    if len(sys.argv) < 4:
        raise Exception(
            'Incorrect number of arguments - usage: [host] [port] [model-path]'
        )
    model.summary()
    uvicorn.run(app, host=sys.argv[1], port=int(sys.argv[2]))
