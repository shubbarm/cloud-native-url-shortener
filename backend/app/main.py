from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from models import get_db, create_short_url, get_original_url

app = FastAPI()

# ✅ CORS middleware must be added AFTER app is created
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Or ["*"] for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: str

@app.options("/shorten", include_in_schema=False)
async def options_shorten(request: Request):
    return JSONResponse(content={}, status_code=200)

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
