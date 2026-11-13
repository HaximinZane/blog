from fastapi import APIRouter
from datetime import datetime,UTC

router = APIRouter(tags=["health-check"])

@router.get("/health")
def health():
    return {"status" : "ok","time" : str(datetime.now(UTC))[0:-16] + " (UTC)"}