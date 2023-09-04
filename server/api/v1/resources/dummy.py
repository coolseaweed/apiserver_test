from fastapi import APIRouter, status
from asyncio import sleep
import random
router = APIRouter()


@router.get(
    "/dummy",
    status_code=status.HTTP_200_OK,
    tags=["dummy"],
)
async def dummy_test() ->str:
    """dummy test endpoint
    it takes random processing time between 0.1 and 0.5 seconds
    """
    sleep_time = random.uniform(0.1, 1.1)
    await sleep(sleep_time)
    if sleep_time > 1.0:
        raise Exception("dummy exception")

    return f"response from dummy endpoint {sleep_time:.2f} sec with proc time"
