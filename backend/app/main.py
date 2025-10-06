from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import get_db, create_short_url, get_original_url


app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/shorten")
def shorten_url(request: URLRequest):
    db = get_db()
    short = create_short_url(db, request.url)
    return {"short_url": short}

@app.get("/{short_code}")
def redirect(short_code: str):
    db = get_db()
    original = get_original_url(db, short_code)
    if not original:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"original_url": original}
