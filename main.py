
from fastapi import FastAPI, APIRouter
from app.routes.note import router

app = FastAPI()

app.include_router(router=router)

@app.get("/")
def root():

    return {"msg": "everything seems working fine"}

