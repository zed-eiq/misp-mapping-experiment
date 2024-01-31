from __future__ import annotations

from typing import Sequence
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, RootModel, constr
from typing_extensions import Annotated

from models.common import (
    MispID,
)


class OrganisationId(RootModel[str]):
    root: Annotated[str, Field(examples=["12345"], max_length=10, pattern="^\\d+$")]


class OrganisationName(RootModel[str]):
    root: Annotated[str, Field(examples=["ORGNAME"], max_length=255)]


class OrganisationNoId(BaseModel):
    name: Annotated[Optional[str], Field(None, examples=["ORGNAME"], max_length=255)]
    date_created: Annotated[
        Optional[str], Field(None, examples=["2021-06-14 14:29:19"])
    ]
    date_modified: Annotated[
        Optional[str], Field(None, examples=["2021-06-14 14:29:19"])
    ]
    description: Optional[str] = None
    type: Annotated[Optional[str], Field(None, examples=["ADMIN"], max_length=255)]
    nationality: Optional[str] = None
    sector: Optional[str] = None
    created_by: MispID
    uuid: Optional[str] = None
    contacts: Optional[str] = None
    local: Optional[bool] = None
    restricted_to_domain: Optional[
        Sequence[
            constr(
                pattern=r"^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]{0,61}[A-Za-z0-9])$"
            )
        ]
    ] = None
    landingpage: Optional[str] = None
    user_count: Annotated[Optional[str], Field(None, examples=["3"], pattern="^\\d+$")]
    created_by_email: Optional[str] = None


class Organisation(OrganisationNoId):
    id: MispID


class OrganisationListItem(BaseModel):
    Organisation: Optional[Organisation] = None


class OrganisationList(RootModel[Sequence[OrganisationListItem]]):
    root: Sequence[OrganisationListItem]


class OrganisationModel(BaseModel):
    id: MispID
    uuid: Optional[UUID]
    name: Annotated[Optional[str], Field(None, examples=["ORGNAME"], max_length=255)]
