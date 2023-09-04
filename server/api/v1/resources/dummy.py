from fastapi import APIRouter, status

router = APIRouter()


@router.get(
    "/dummy",
    status_code=status.HTTP_200_OK,
    tags=["dummy"],
)
async def dummy_test() ->str:
    """health check endpoint

    Returns
    -------
    health.HealthResponse
        return 'ok' response after checking db
    """

    return "response from dummy test"
