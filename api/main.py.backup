from fastapi import FastAPI
import uvicorn
from mylib import hello, greet, add_numbers, get_library_info

app = FastAPI(title="Sample UV Library", version="0.1.0")


@app.get("/")
async def root():
    return {"message": hello()}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/info")
async def info():
    return get_library_info()


@app.get("/greet/{name}")
async def greet_user(name: str):
    return {"message": greet(name)}


@app.get("/add/{a}/{b}")
async def add(a: int, b: int):
    result = add_numbers(a, b)
    return {"result": result, "calculation": f"{a} + {b} = {result}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)