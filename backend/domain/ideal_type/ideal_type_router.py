from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/ideal_type"
)


@router.get("/")
def get_ideal_type_score():
    return {'similarity': 0.5}

