from fastapi import FastAPI
import uvicorn
app=FastAPI()
@app.get("/")
def fun():
    return "hello world"