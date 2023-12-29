import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.job import job_router
from domain.ideal_type import ideal_type_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(job_router.router)
app.include_router(ideal_type_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)