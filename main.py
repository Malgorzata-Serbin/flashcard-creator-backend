from fastapi import FastAPI
import ollama

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ollamaTest")
async def ollamaTest():
    model = ollama.generate(model='gemma3:12b-it-qat', prompt='who is bingus?')
    return {"response": model}