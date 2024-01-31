from __future__ import annotations

from typing import Sequence
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, RootModel
from typing_extensions import Annotated

from models.common import (
    MispID,
    AnalysisLevelId,
    DistributionLevelId,
    ThreatLevelId,
)
from models.users import UserNoId


class EventReport(BaseModel):
    pass


class EventOrganisation(BaseModel):
    id: MispID
    name: Annotated[Optional[str], Field(None, examples=["ORGNAME"], max_length=255)]
    uuid: Optional[UUID]


class Event(BaseModel):
    id: MispID = None
    """It is possible to have an event with no id. Probably on creation"""

    org_id: MispID
    distribution: Optional[DistributionLevelId] = None
    info: Annotated[
        Optional[str], Field(None, examples=["logged source ip"], max_length=65535)
    ]
    orgc_id: MispID
    uuid: Optional[UUID]
    date: Annotated[Optional[str], Field(None, examples=["1991-01-15"])]
    published: Optional[bool] = None
    analysis: Optional[AnalysisLevelId] = None
    attribute_count: Annotated[
        Optional[str], Field(None, examples=["321"], pattern="^\\d+$")
    ]
    timestamp: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$|^$")
    ]
    sharing_group_id: Annotated[
        Optional[str], Field(None, examples=["1"], max_length=10, pattern="^\\d+$|^$")
    ]
    proposal_email_lock: Optional[bool] = None
    locked: Optional[bool] = None
    threat_level_id: Optional[ThreatLevelId] = None
    publish_timestamp: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]
    sighting_timestamp: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]
    disable_correlation: Optional[bool] = None
    extends_uuid: Annotated[
        Optional[str],
        Field(None, examples=["c99506a6-1255-4b71-afa5-7b8ba48c3b1b"], max_length=36),
    ]
    event_creator_email: Optional[EmailStr] = None


class SlimEvent(BaseModel):
    id: Annotated[str, Field(examples=["12345"], max_length=10, pattern="^\\d+$")]
    timestamp: Annotated[str, Field(examples=["1617875568"], pattern="^\\d+$")]
    sighting_timestamp: Annotated[str, Field(examples=["1617875568"], pattern="^\\d+$")]
    published: bool
    uuid: Annotated[
        UUID, Field(examples=["c99506a6-1255-4b71-afa5-7b8ba48c3b1b"], max_length=36)
    ]
    orgc_uuid: Annotated[
        UUID, Field(examples=["c99506a6-1255-4b71-afa5-7b8ba48c3b1b"], max_length=36)
    ]


class EventList(RootModel[Sequence[Event]]):
    root: Sequence[Event]


class SlimEventList(RootModel[Sequence[SlimEvent]]):
    root: Sequence[SlimEvent]


class Event4(BaseModel):
    id: MispID
    info: Annotated[
        Optional[str], Field(None, examples=["logged source ip"], max_length=65535)
    ]
    org_id: MispID
    orgc_id: MispID


class EventTag(BaseModel):
    id: MispID
    event_id: MispID
    tag_id: MispID
    local: Optional[bool] = None
    Tag: Optional[Tag] = None


class EventTagList(RootModel[Sequence[EventTag]]):
    root: Sequence[EventTag]


class ExtendedTaxonomyEntry(UserNoId):
    events: Optional[float] = None
    attributes: Optional[float] = None


class RelatedEventItem(BaseModel):
    Event: Optional[ExtendedEvent] = None


class ExtendedEvent(Event):
    Feed: Optional[Feed] = None
    Org: Optional[EventOrganisation] = None
    Orgc: Optional[EventOrganisation] = None
    Attribute: Optional[Sequence[Attribute]] = None
    ShadowAttribute: Optional[Sequence[Attribute]] = None
    RelatedEvent: Optional[Sequence[RelatedEventItem]] = None
    Galaxy: Optional[Sequence[Galaxy]] = None
    Object: Optional[Sequence[Object]] = None
    EventReport: Optional[Sequence[EventReport]] = None
    Tag: Optional[Sequence[Tag]] = None


class CreatedEvent(BaseModel):
    Event: Optional[CreatedEventSchema] = None


class CreatedEventSchema(ExtendedEvent):
    event_creator_email: Optional[EmailStr] = None
    Galaxy: Optional[Sequence[Galaxy]] = None
    Object: Optional[Sequence[Object]] = None
    EventReport: Optional[Sequence[EventReport]] = None


class UpdatedEvent(BaseModel):
    Event: Optional[UpdatedEventSchema] = None


class UpdatedEventSchema(ExtendedEvent):
    event_creator_email: Optional[EmailStr] = None
    Galaxy: Optional[Sequence[Galaxy]] = None
    Object: Optional[Sequence[Object]] = None
    EventReport: Optional[Sequence[EventReport]] = None
    Tag: Optional[Sequence[Tag]] = None


class ExtendedEventList(RootModel[Sequence[ExtendedEvent]]):
    root: Sequence[ExtendedEvent]


class EventRestSearchListItem(BaseModel):
    Event: Optional[EventRestSearchListItemResult] = None


class EventRestSearchListItemResult(ExtendedEvent):
    Event: Optional[SlimEvent] = None


class EventRestSearchList(RootModel[Sequence[EventRestSearchListItem]]):
    root: Sequence[EventRestSearchListItem]


RelatedEventItem.model_rebuild()
CreatedEvent.model_rebuild()
UpdatedEvent.model_rebuild()
EventRestSearchListItem.model_rebuild()
