#Import du framework
from fastapi import FastAPI

#Import de la Documentation
from documentation.description import api_description
from documentation.tags import tags_metadata

#Import du router
import routers.ShopSmart

#Initialisation de l'API
app = FastAPI(
    title="ShopSmart",
    description=api_description,
    openapi_tags=tags_metadata
)

app.include_router(routers.ShopSmart.router)