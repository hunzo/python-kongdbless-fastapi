from fastapi import FastAPI

app = FastAPI(title="fast api")

@app.get("/")
def main():
    return {
        "status": "success"
    }