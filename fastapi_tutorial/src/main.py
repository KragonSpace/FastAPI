from fastapi import FastAPI

# import subrouter - multiple router
from .web import explorer

app = FastAPI()

# import subrouter - multiple router
app.include_router(explorer.router)


@app.get("/")
def top():
    return "top here"

# Path Parameter
@app.get('/echo/{thing}')
def echo(thing):
    return f'echoing {thing}'

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', reload=True)