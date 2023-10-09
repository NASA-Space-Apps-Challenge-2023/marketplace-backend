import strawberry
from typing import List, Optional
from server.database import keyword as keyword_db


@strawberry.type
class Keyword:
    id: str
    keyword: str


@strawberry.type
class KeywordQuery:
    @strawberry.field
    async def keywords(self, id: Optional[str] = None) -> List[Keyword]:
        if id:
            # Handle retrieval by id
            pass
        keywords_from_db = await keyword_db.retrieve_keywords()
        return [Keyword(id=k["id"], keyword=k["keyword"]) for k in keywords_from_db]


@strawberry.type
class KeywordMutation:
    @strawberry.mutation
    async def add_keyword(self, keyword: str) -> Keyword:
        new_keyword_data = await keyword_db.add_keyword({"keyword": keyword})
        return Keyword(id=new_keyword_data["id"], keyword=new_keyword_data["keyword"])

    # Additional mutations like update or delete can be added here


# schema = strawberry.Schema(query=KeywordQuery, mutation=KeywordMutation)
