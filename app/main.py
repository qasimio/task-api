from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"],
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
    }
    