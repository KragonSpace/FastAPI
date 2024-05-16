from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware ### CORS

# File
from pathlib import Path
from typing import Generator
# File upload using File()
from fastapi import File
# File upload using UploadFile - large size
from fastapi import UploadFile
# File Download
from fastapi.responses import FileResponse
# File Download large files
from fastapi.responses import StreamingResponse
# Static File
from fastapi.staticfiles import StaticFiles

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

# File Upload - small size
@app.post("/small")
async def upload_small_file(small_file: bytes = File()) -> str:
    return f"file size: {len(small_file)}"

# File Upload - big size
@app.post("/big")
async def upload_big_file(big_file: UploadFile) -> str:
    return f"file size: {big_file.size}, name: {big_file.filename}"

# File download
@app.get("/small/{name}")
async def download_small_file(name):
    return FileResponse(name)

# File Download - large size
def gen_file(path: str) -> Generator:
    with open(file=path, mode="rb") as file:
        yield file.read()

@app.get("/download_big/{name}")
async def download_big_file(name:str):
    gen_expr = gen_file(file_path=Path)
    response = StreamingResponse(
                content=gen_expr,
                status_code=200,
            )
    return response
# Static File
# Directory containing main.py:
top = Path(__file__).resolve.parent
app.mount("/static",
            StaticFiles(directory=f"{top}/static", html=True),
            name="free")

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