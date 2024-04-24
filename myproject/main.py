from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter
from Myproject.views import app1
from Myproject import views


app = FastAPI()

app.include_router(app1,prefix='/user',tags=["settings"])

if __name__ == "__main__":    
    uvicorn.run(app, host="127.0.0.1", port=8000)