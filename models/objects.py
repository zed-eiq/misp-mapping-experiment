from __future__ import annotations

from collections.abc import Sequence
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from common import (
    MispID,
    DistributionLevelId,
)
from events import Event4


class ObjectRelationshipType(BaseModel):
    # See object-relationship.json
    # or https://github.com/MISP/misp-objects/blob/main/relationships/definition.json
    name: str
    oppposite: str  # Name of relationship in reverse direction
    format: List[str]
    # Omitted description -- not important for usage


class Object(BaseModel):
    id: MispID
    name: Annotated[
        Optional[str], Field(None, examples=["ail-leak"], max_length=131071)
    ]
    meta_category: Annotated[Optional[str], Field(None, alias="meta-category")]
    description: Optional[str] = None
    template_uuid: Optional[UUID]
    template_version: Annotated[
        Optional[str], Field(None, examples=["1"], pattern="^\\d+$")
    ]
    event_id: MispID
    uuid: Optional[UUID]
    timestamp: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]
    distribution: Optional[DistributionLevelId] = None
    sharing_group_id: Annotated[
        Optional[str], Field(None, examples=["1"], max_length=10, pattern="^\\d+$|^$")
    ]
    comment: Optional[str] = None
    deleted: Optional[bool] = None
    first_seen: Annotated[
        Optional[str], Field(None, examples=["1581984000000000"], pattern="^\\d+$|^$")
    ]
    last_seen: Annotated[
        Optional[str], Field(None, examples=["1581984000000000"], pattern="^\\d+$|^$")
    ]
    Attribute: Optional[Sequence[Attribute]] = None


class ExtendedObject(Object):
    Event: Optional[Event4] = None
