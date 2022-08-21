from fastapi import FastAPI, UploadFile, File
from os import getcwd

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/archivo")
async def convertir_archivo_crear_peracion(file: UploadFile = File(...)):
    with open(getcwd() + "/" + file.filename, "wb") as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()
    return content

@app.post("/archivoo")
async def convertir(file: UploadFile = File(...)):
    with open(getcwd() + "/" + file.filename, "wb") as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()
    data = content.decode()
    return data

