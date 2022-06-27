from fastapi import FastAPI
import uvicorn

app = FastAPI()


def configure():
  pass
    
@app.get("/")
async def ping():
  return {"msg": "ping"}


if __name__=="__main__":
    configure()
    uvicorn.run('main:app', reload=True)
else:
    configure()