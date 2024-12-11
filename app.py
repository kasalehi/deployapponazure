from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def fun():
    return "hello world"