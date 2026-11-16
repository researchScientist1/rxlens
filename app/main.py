from fastapi import FastAPI
app = FastAPI(title="RxLens")

@app.get("/health")
def health():
    return {"status": "ok"}