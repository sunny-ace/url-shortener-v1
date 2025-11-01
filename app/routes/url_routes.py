from fastapi import APIRouter, Request, Form
#from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import string, random

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

url_db = {}

def create_short_code(length=6):
 char = string.ascii_letters + string.digits
 return ''.join(random.choice(char) for _ in range(length))

@router.get("/")
def home(request: Request):
 return templates.TemplateResponse("index.html", {"request": request})

@router.post("/shorten")
def shorten_url(request: Request, long_url : str = Form(...)):
 short_code = create_short_code()
 url_db[short_code] = long_url
 return templates.TemplateResponse("index.html", {"request": request, "shortened_url": f"http://127.0.0.1:8000/{short_code}" })

@router.get("/{short_code}")
def redirect_short_url(short_code : str):
 if short_code in url_db:
  return RedirectResponse(url_db[short_code])
 return {"error:" "Short URL not found"}

@router.get("/{short_code}")
def redirect_url(short_code:str):
 if short_code in url_db:
  long_url = url_db[short_code]
  return RedirectResponse(long_url)
 return {"error:" "Short URL not found"}