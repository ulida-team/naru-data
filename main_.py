from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.job import job_router
from domain.ai import user_feature_similarity


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(job_router.router)
app.include_router(user_feature_similarity.router)
