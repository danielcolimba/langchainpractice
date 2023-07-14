from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.get("/process")
async def root():
    return {"message": "Hello World"}

@app.post("/upload")
async def read_root(doc: UploadFile = File(...)):
    with open("base.pdf", "wb") as f:
        f.write(doc.file, f)
    await doc.close()
    return {"response": file.filename}
    
# Aplicativo de la prueba integrar con el modelo y la api 