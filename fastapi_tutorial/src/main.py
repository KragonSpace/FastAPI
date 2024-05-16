from fastapi import FastAPI

# import subrouter - multiple router
from web import explorer, creature

app = FastAPI()

# import subrouter - multiple endpoints
app.include_router(explorer.router)
app.include_router(creature.router)

# Test Endpoints
# @app.get("/")
# def top():
#     return "top here"

# # Path Parameter
# @app.get('/echo/{thing}')
# def echo(thing):
#     return f'echoing {thing}'

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', reload=True)