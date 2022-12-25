## Server: Uvicorn & FastAPI

This repository contains the necessary files to set up a simple HTTP backend for serving results from the model. Uvicorn is used to set up the web server and FastAPI to set up the API endpoints. 

### Installation 

#### 1. Virtual Environment
It is highly recommended - yet optional - to create a virtual environment before executing this project. This can be done simply by running 

`python3 -m venv .venv`

The file `requirements.txt` contains all dependencies. These can be installed with 

`pip install -r requirements.txt`

#### 2. Initialization

The entry point for the module is `main.py`. It receives three compulsory parameters. 
1. A host, e.g. 127.0.0.1.
2. A port, e.g. 8080.  
3. A path to the model, generated in the `model` module of this project. 

#### 3. API

The API consists of a single endpoint, `/images`, which accepts `POST` requests. 

At the time, only jpeg, jpg, and png image formats are guaranteed to be supported. 

A `POST` request to `/images` may be as follows: 

    curl -X 'POST' \
        'http://127.0.0.166:8080/images' \
        -H 'accept: application/json' \
        -H 'Content-Type: multipart/form-data' \
        -F 'file=@picture.jpg;type=image/jpeg'

The `Content-Type` of the `POST` data must be `multipart/form-data`, according to [RFC 2388](https://www.rfc-editor.org/rfc/rfc2388).

