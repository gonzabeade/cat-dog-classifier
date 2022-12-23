from fastapi import FastAPI, Header, Depends, \
     HTTPException, status, File, UploadFile
import uvicorn
import sys
import tensorflow as tf

# Uninstall flake8

app = FastAPI()
model = None
valid_image_types = ["png", "jpeg", "jpg"]


def val_content_type(content_type: str = Header(default="")):
    """
        Validates the request content-type to be image/png
    """
    type = content_type.split("/")
    if type[0] != "image" or type[1] not in valid_image_types:
        raise HTTPException(
            status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            f"Unsupported media type: {content_type}."
        )


@app.get("/images", dependencies=[Depends(val_content_type)])
async def images(
    my_file: UploadFile = File(...),
):
    return {"message": "Hello World"}


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
    uvicorn.run(app, host=sys.argv[1], port=int(sys.argv[2]))
