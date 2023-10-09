import strawberry
from .keyword import KeywordQuery, KeywordMutation
from .project import ProjectQuery, ProjectMutation
from strawberry.schema.config import StrawberryConfig


@strawberry.type
class Query(KeywordQuery, ProjectQuery):
    pass


@strawberry.type
class Mutation(KeywordMutation, ProjectMutation):
    pass


schema = strawberry.Schema(
    query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=False))
