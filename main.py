from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"messaggio": "Enterprise Knowledge Assistant è attivo"}