from fastapi import FASTAPI


app = fastapi()

@app.get("/")
def getPost():
    return "Hello world!"