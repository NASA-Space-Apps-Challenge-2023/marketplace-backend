from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes.user import router as UserRouter
from server.routes.authentication import router as AuthRouter
from server.routes.project import router as ProjectRouter
from server.routes.keyword import router as KeywordRouter
from server.routes.discussion import router as DiscussionRouter
from fastapi.staticfiles import StaticFiles
from strawberry.fastapi import GraphQLRouter
from server.graphql.schema import schema
from decouple import config

is_production = config('PROJECT_ENVIRONMENT', default="DEVELOPMENT")

if is_production == 'RELEASE':
    app = FastAPI(
        docs_url=None,  # Disable docs (Swagger UI)
        redoc_url=None,  # Disable redoc
    )
else:
    app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(AuthRouter, tags=["Authentication"])
app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(ProjectRouter, tags=["Project"], prefix="/project")
app.include_router(KeywordRouter, tags=["Keyword"], prefix="/keyword")
app.include_router(DiscussionRouter, tags=["Discussion"], prefix="/discussion")
app.include_router(
    GraphQLRouter(schema=schema),
    prefix="/graphql",
    tags=["GraphQL"]
)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Scicollab API!"}
