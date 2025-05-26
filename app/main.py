from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.utils.load_runner import run_load_test
from app.schemas import LoadTestRequest

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def serve_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/load-test")
async def load_test(data: LoadTestRequest):
    result = run_load_test(data)
    return result
