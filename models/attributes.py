from __future__ import annotations

from typing import Optional
from typing import Sequence
from uuid import UUID

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Annotated

from common import (
    MispID,
    AttributeType,
    AttributeCategory,
    DistributionLevelId,
)
from decay import DecayScore


class AttributeEventUUID(RootModel[UUID]):
    root: Annotated[
        UUID, Field(examples=["c99506a6-1255-4b71-afa5-7b8ba48c3b1b"], max_length=36)
    ]


class AttributeNoId(BaseModel):
    event_id: MispID
    object_id: MispID
    object_relation: Annotated[
        Optional[str], Field(None, examples=["sensor"], max_length=255)
    ]
    category: Optional[AttributeCategory] = None
    type: Optional[AttributeType] = None
    value: Annotated[
        Optional[str], Field(None, examples=["127.0.0.1"], max_length=131071)
    ]
    to_ids: Optional[bool] = None
    uuid: Optional[UUID]
    timestamp: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$|^$")
    ]
    distribution: Optional[DistributionLevelId] = None
    sharing_group_id: Annotated[
        Optional[str], Field(None, examples=["1"], max_length=10, pattern="^\\d+$|^$")
    ]
    comment: Annotated[
        Optional[str], Field(None, examples=["logged source ip"], max_length=65535)
    ]
    deleted: Optional[bool] = None
    disable_correlation: Optional[bool] = None
    first_seen: Annotated[
        Optional[str], Field(None, examples=["1581984000000000"], pattern="^\\d+$|^$")
    ]
    last_seen: Annotated[
        Optional[str], Field(None, examples=["1581984000000000"], pattern="^\\d+$|^$")
    ]


class Attribute(AttributeNoId):
    id: MispID


class ExtendedAttribute(Attribute):
    data: Optional[str] = None
    """
    base64 representation of the attachment
    """
    event_uuid: Optional[UUID]
    decay_score: Optional[Sequence[DecayScore]] = None
