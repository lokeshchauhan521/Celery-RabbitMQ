from fastapi import FastAPI
from .tasks import add , multi
from celery.result import AsyncResult

app = FastAPI()

@app.get("/add/")
def trigger_add(x: int, y: int):
    result = add.delay(x, y)  
    return {"result_id": result.id}

@app.get("/multi")
def multiple(x , y ):
    result  = multi(x, y)
    return {"result":result.id}


@app.get("/result/{task_id}")
def get_result(task_id: str):
    result = AsyncResult(task_id)
    if result.ready():
        return {"status": result.status, "result": result.result}
    else:
        return {"status": result.status}

#This is test