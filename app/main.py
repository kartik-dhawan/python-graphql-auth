from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.graphql.router import graphql_app

app = FastAPI()


app.include_router(graphql_app, prefix='/graphql')


@app.get('/health')
async def health():
    return {"ok": False}
