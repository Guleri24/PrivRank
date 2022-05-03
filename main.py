from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def input_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def recommended_users(request: Request,
                                liked_users: str = Form(...)):
    recommended_users_arr = liked_users.split(",")

    # add recommended users logic here


    delim = ','
    recommended_users_str = delim.join(map(str, recommended_users_arr))
    return recommended_users_str
    # return templates.TemplateResponse("form.html", {"request": request})