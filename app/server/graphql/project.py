import strawberry
from typing import List, Optional
from server.database import project as project_db


@strawberry.type
class Project:
    id: str
    project_name: str
    project_url_on_catalog: Optional[str]
    project_url_external: Optional[str]
    project_description: str
    keywords: List[str]
    fields_of_science: List[str]
    project_status: str
    agency_sponsor: Optional[str]
    agency_sponsor_other: Optional[str]
    gov_contact: Optional[str]
    gov_contact_email: Optional[str]
    geographic_scope: Optional[str]
    participant_age: Optional[str]
    participation_tasks: List[str]
    scistarter: Optional[str]
    email: str
    start_date: str
    project_goals: Optional[str]
    stars: int
    collaborators: Optional[List[str]]
    owner_id: str
    discussions: Optional[List[str]]


@strawberry.type
class ProjectQuery:
    @strawberry.field
    async def projects(self, id: Optional[str] = None) -> List[Optional[Project]]:
        if id:
            project = await project_db.retrieve_project(id)
            print(f"Single Project Data: {project}")  # Debug print
            return [project]
        projects = await project_db.retrieve_projects()
        print(f"All Projects Data: {projects}")  # Debug print
        return projects


@strawberry.input
class ProjectInput:
    project_name: str
    project_url_on_catalog: Optional[str]
    project_url_external: Optional[str]
    project_description: str
    keywords: List[str]
    fields_of_science: List[str]
    project_status: str
    agency_sponsor: Optional[str]
    agency_sponsor_other: Optional[str]
    gov_contact: Optional[str]
    gov_contact_email: Optional[str]
    geographic_scope: Optional[str]
    participant_age: Optional[str]
    participation_tasks: List[str]
    scistarter: Optional[str]
    email: str
    start_date: str
    project_goals: Optional[str]
    stars: int
    collaborators: Optional[List[str]]
    owner_id: str
    discussions: Optional[List[str]]


@strawberry.type
class ProjectMutation:
    @strawberry.mutation
    async def add_project(self, input: ProjectInput) -> Project:
        project_data = input.dict()
        new_project_data = await project_db.add_project(project_data)
        return Project(**new_project_data)
