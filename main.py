import strawberry
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from fb_data.fb_queries import FB_Queries
from user_app.graph_ql_mutation import Mutation
from sql_app import models
from sql_app.database import engine
from sql_app.mongo_db_conf import MongoDbConf



if __name__ == "__main__":
    load_dotenv()
    models.Base.metadata.create_all(bind=engine)
    mongo_db = MongoDbConf().connect()

    @strawberry.type
    class Query:
        @strawberry.field
        def hello(self) -> str:
            return "Hello World"


    user_schema = strawberry.Schema(query=Query, mutation=Mutation)
    fb_schema = strawberry.Schema(query=FB_Queries)
    graphql_app = GraphQLRouter(user_schema)
    fb_apis = GraphQLRouter(fb_schema)
    app = FastAPI()
    app.include_router(graphql_app, prefix="/user")
    app.include_router(fb_apis, prefix="/fb_data")
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)