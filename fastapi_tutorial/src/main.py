from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware ### CORS

# import subrouter - multiple router
from web import explorer, creature, user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ui.cryptids.com",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_header=["*"],
)
# import subrouter - multiple endpoints
app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(user.router)

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