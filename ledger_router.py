from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_ledger():
    return {"message": "This is the ledger endpoint."} 