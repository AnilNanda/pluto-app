from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def getPost():
    return "Hello world!"

def add(a, b):
    return a+b
