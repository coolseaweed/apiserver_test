import asyncio
import dataclasses
import os

from fastapi import APIRouter, FastAPI, Depends

from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRoute
from loguru import logger

from server.api.v1.routes import api_router as api_v1_router
from server.core.config import config
from server.version import app_title, app_description, version_info, version_number



swagger_router = APIRouter()


# create a custom endpoint to allow swagger access through eks
@swagger_router.get("/openapi.json", include_in_schema=False)
@swagger_router.get(config.openapi_url, include_in_schema=False)
def access_openapi():
    logger.debug("calling openapi.json")
    openapi = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
        tags=app.openapi_tags,
    )
    openapi["servers"] = [{"url": config.server_path}]
    return openapi


# create the app itself with CORS support
def create_app():
    # create fastapi app
    app = FastAPI(
        root_path=config.root_path,
        openapi_url=config.openapi_url,
        docs_url=config.swagger_url,
        debug=True,
        title=app_title,
        description=app_description,
    )

    # include the main endpoint router
    app.include_router(api_v1_router)
    app.include_router(swagger_router)

    return app


# log all configuration parameters
for k, v in dataclasses.asdict(config).items():
    logger.info(f"{k:>24} : {v} ({type(v).__name__})")


# display version info
logger.debug(f"version: {version_number}")
logger.debug(f"feature: {version_info}")
app = create_app()
