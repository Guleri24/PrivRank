import csv
import re
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
    recommended_users_arr = liked_users.split(',')
    recommended_users_arr = [int(e) for e in recommended_users_arr]

    # add recommended users logic here
    recommended_users_arr = predict(recommended_users_arr)
    res = ''
    for id, score in recommended_users_arr:
        res += f'Recommending item number {id} having prediction score {score} <br>'
    return res
    #return '\n'.join(str(e) for e in recommended_users_arr)

    # delim = ','
    # recommended_users_str = delim.join(map(str, recommended_users_arr))
    # return recommended_users_str
    # return templates.TemplateResponse("form.html", {"request": request})

def predict(arr):
    arr = set(arr)
    matrix = get_similarity_matrix()
    N = len(matrix)

    scores = [[0,i] for i in range(0,N)]
    for liked_item in arr:
        for idx in range(0,N):
            scores[idx][0] += matrix[liked_item][idx]
    scores.sort(reverse=True)
    res = []
    for score,val in scores:
        if val not in arr: res += [[val,score]]
        if len(res) == 10: break
    return res

def get_similarity_matrix():
    with open('similarity.csv', newline='') as file:
        reader = csv.reader(file,delimiter=' ')
        matrix = []
        for row in reader:
            matrix += [[float(e) for e in row]]   
        return matrix
