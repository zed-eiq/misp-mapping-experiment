from __future__ import annotations

from collections.abc import Sequence
from enum import Enum
from typing import Optional, Union
from uuid import UUID

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Annotated

from attributes import ExtendedAttribute
from common import (
    MispID,
    AttributeType,
    AttributeCategory,
    ThreatLevelId,
)
from decay import DecayingModelParameters
from organisation import OrganisationId, OrganisationName


class ObjectRestSearchList(BaseModel):
    Object: Optional[Object] = None


class ObjectsRestSearchReturnFormat(str, Enum):
    JSON = "json"


class EventsRestSearchReturnFormat(str, Enum):
    JSON = "json"
    XML = "xml"
    CSV = "csv"
    TEXT = "text"
    STIX = "stix"
    STIX2 = "stix2"
    STIX_JSON = "stix-json"
    ATTACK = "attack"
    ATTACK_SIGHTINGS = "attack-sightings"
    CACHE = "cache"
    COUNT = "count"
    HASHES = "hashes"
    NETFILTER = "netfilter"
    OPENDATA = "opendata"
    OPENIOC = "openioc"
    RPZ = "rpz"
    SNORT = "snort"
    SURICATA = "suricata"
    YARA = "yara"
    YARA_JSON = "yara-json"


class AttributesRestSearchReturnFormat(str, Enum):
    JSON = "json"
    XML = "xml"
    CSV = "csv"
    TEXT = "text"
    HASHES = "hashes"
    CACHE = "cache"
    COUNT = "count"
    NETFILTER = "netfilter"
    OPENDATA = "opendata"
    OPENIOC = "openioc"
    RPZ = "rpz"
    SNORT = "snort"
    SURICATA = "suricata"
    text_1 = "text"
    YARA = "yara"
    YARA_JSON = "yara-json"


class ObjectRestSearchFilter(BaseModel):
    page: Annotated[Optional[int], Field(None, ge=1)]
    limit: Annotated[Optional[int], Field(None, ge=0)]
    quickFilter: Annotated[Optional[str], Field(None, examples=["malware"])]
    """
    Search events by matching any tag names, event descriptions, attribute values or attribute comments
    """
    searchall: Annotated[Optional[str], Field(None, examples=["malware"])]
    """
    Search events by matching any tag names, event descriptions, attribute values or attribute comments
    """
    timestamp: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]
    object_name: Annotated[
        Optional[str], Field(None, examples=["ail-leak"], max_length=131071)
    ]
    object_template_uuid: Optional[UUID]
    object_template_version: Annotated[
        Optional[str], Field(None, examples=["1"], pattern="^\\d+$")
    ]
    eventid: MispID
    eventinfo: Annotated[
        Optional[str], Field(None, examples=["logged source ip"], max_length=65535)
    ]
    ignore: Optional[bool] = False
    """
    If true matches both true and false values for `to_ids` and `published`
    """
    from_: Annotated[Optional[str], Field(None, alias="from")]
    """
    You can use any of the valid time related filters (examples: 7d, timestamps, [14d, 7d] for ranges, etc.)
    """
    to: Optional[str] = None
    """
    You can use any of the valid time related filters (examples: 7d, timestamps, [14d, 7d] for ranges, etc.)
    """
    date: Optional[str] = None
    """
    You can use any of the valid time related filters (examples: 7d, timestamps, [14d, 7d] for ranges, etc.)
    """
    tags: Optional[Sequence[str]] = None
    last: Optional[Union[int, str]] = None
    """
    Events published within the last x amount of time, where x can be defined in days, hours, minutes (for example 5d or 12h or 30m), ISO 8601 datetime format or timestamp
    """
    event_timestamp: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]
    publish_timestamp: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]
    org: Optional[Union[OrganisationId, OrganisationName]] = None
    uuid: Optional[UUID]
    value: Annotated[
        Optional[str], Field(None, examples=["127.0.0.1"], max_length=131071)
    ]
    type: Optional[AttributeType] = None
    category: Optional[AttributeCategory] = None
    object_relation: Annotated[Optional[str], Field(None, examples=["filepath"])]
    """
    Filter by the attribute object relation value
    """
    attribute_timestamp: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]
    first_seen: Annotated[
        Optional[str], Field(None, examples=["1581984000000000"], pattern="^\\d+$|^$")
    ]
    last_seen: Annotated[
        Optional[str], Field(None, examples=["1581984000000000"], pattern="^\\d+$|^$")
    ]
    comment: Annotated[
        Optional[str], Field(None, examples=["logged source ip"], max_length=65535)
    ]
    to_ids: Optional[bool] = None
    published: Optional[bool] = None
    deleted: Optional[bool] = None
    withAttachments: Optional[bool] = None
    """
    Extends the response with the base64 representation of the attachment, if there is one
    """
    enforceWarninglist: Optional[bool] = None
    """
    Should the warning list be enforced. Adds blocked field for matching attributes
    """
    includeAllTags: Optional[bool] = None
    """
    Include also exportable tags
    """
    includeEventUuid: Optional[bool] = None
    """
    Include matching eventUuids in the response
    """
    include_event_uuid: Optional[bool] = None
    """
    Include matching eventUuids in the response
    """
    includeEventTags: Optional[bool] = None
    """
    Include tags of matching events in the response
    """
    includeProposals: Optional[bool] = None
    """
    Include proposals of matching events in the response
    """
    includeWarninglistHits: Optional[bool] = None
    includeContext: Optional[bool] = None
    """
    Adds events context fields in the CSV export
    """
    includeSightings: Optional[bool] = None
    """
    Adds events context fields in the CSV export
    """
    includeSightingdb: Optional[bool] = None
    """
    Extend response with Sightings DB results if the module is enabled
    """
    includeCorrelations: Optional[bool] = None
    includeDecayScore: Optional[bool] = None
    """
    Include all enabled decaying score
    """
    includeFullModel: Optional[bool] = None
    """
    Include all model information of matching events in the response
    """
    allow_proposal_blocking: Optional[bool] = None
    """
    Allow blocking attributes from to_ids sensitive exports if a proposal has been made to it to remove the IDS flag
    """
    metadata: Optional[bool] = None
    """
    Will only return the metadata of the given query scope, contained data is omitted.
    """
    attackGalaxy: Annotated[Optional[str], Field(None, examples=["mitre-attack"])]
    excludeDecayed: Optional[bool] = None
    """
    Should the decayed elements by excluded
    """
    decayingModel: Optional[str] = None
    """
    Specify the decaying model from which the decaying score should be calculated
    """
    modelOverrides: Optional[DecayingModelParameters] = None
    score: Optional[str] = None
    """
    An alias to override on-the-fly the threshold of the decaying model
    """
    returnFormat: Optional[ObjectsRestSearchReturnFormat] = None


class AttributeRestSearchFilter(BaseModel):
    page: Annotated[Optional[int], Field(None, ge=1)]
    limit: Annotated[Optional[int], Field(None, ge=0)]
    value: Annotated[
        Optional[str], Field(None, examples=["127.0.0.1"], max_length=131071)
    ]
    value1: Annotated[
        Optional[str], Field(None, examples=["127.0.0.1"], max_length=131071)
    ]
    value2: Annotated[
        Optional[str], Field(None, examples=["127.0.0.1"], max_length=131071)
    ]
    type: Optional[AttributeType] = None
    category: Optional[AttributeCategory] = None
    org: Optional[Union[OrganisationId, OrganisationName]] = None
    tags: Optional[Sequence[str]] = None
    from_: Annotated[Optional[str], Field(None, alias="from")]
    """
    You can use any of the valid time related filters (examples: 7d, timestamps, [14d, 7d] for ranges, etc.)
    """
    to: Optional[str] = None
    """
    You can use any of the valid time related filters (examples: 7d, timestamps, [14d, 7d] for ranges, etc.)
    """
    last: Optional[Union[int, str]] = None
    """
    Events published within the last x amount of time, where x can be defined in days, hours, minutes (for example 5d or 12h or 30m), ISO 8601 datetime format or timestamp
    """
    eventid: MispID
    withAttachments: Optional[bool] = None
    """
    Extends the response with the base64 representation of the attachment, if there is one
    """
    uuid: Optional[UUID]
    publish_timestamp: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]
    published: Optional[bool] = None
    timestamp: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]
    attribute_timestamp: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]
    enforceWarninglist: Optional[bool] = None
    """
    Should the warning list be enforced. Adds blocked field for matching attributes
    """
    to_ids: Optional[bool] = None
    deleted: Optional[bool] = None
    event_timestamp: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]
    threat_level_id: Optional[ThreatLevelId] = None
    eventinfo: Optional[str] = None
    """
    Quick event description
    """
    sharinggroup: Optional[Sequence[str]] = None
    """
    Sharing group ID(s), either as single string or list of IDs
    """
    decayingModel: Optional[str] = None
    """
    Specify the decaying model from which the decaying score should be calculated
    """
    score: Optional[str] = None
    """
    An alias to override on-the-fly the threshold of the decaying model
    """
    first_seen: Optional[str] = None
    """
    Seen within the last x amount of time, where x can be defined in days, hours, minutes (for example 5d or 12h or 30m)
    """
    last_seen: Optional[str] = None
    """
    Seen within the last x amount of time, where x can be defined in days, hours, minutes (for example 5d or 12h or 30m)
    """
    includeEventUuid: Optional[bool] = None
    """
    Include matching eventUuids in the response
    """
    includeEventTags: Optional[bool] = None
    """
    Include tags of matching events in the response
    """
    includeProposals: Optional[bool] = None
    """
    Include proposals of matching events in the response
    """
    requested_attributes: Optional[Sequence[str]] = None
    """
    List of properties that will be selected in the CSV export
    """
    includeContext: Optional[bool] = None
    """
    Adds events context fields in the CSV export
    """
    headerless: Optional[bool] = None
    """
    Removes header in the CSV export
    """
    includeWarninglistHits: Optional[bool] = None
    attackGalaxy: Annotated[Optional[str], Field(None, examples=["mitre-attack"])]
    object_relation: Annotated[Optional[str], Field(None, examples=["filepath"])]
    """
    Filter by the attribute object relation value
    """
    includeSightings: Optional[bool] = None
    """
    Extend response with Sightings DB results if the module is enabled
    """
    includeCorrelations: Optional[bool] = None
    modelOverrides: Optional[DecayingModelParameters] = None
    includeDecayScore: Optional[bool] = None
    """
    Include all enabled decaying score
    """
    includeFullModel: Optional[bool] = None
    """
    Include all model information of matching events in the response
    """
    excludeDecayed: Optional[bool] = None
    """
    Should the decayed elements by excluded
    """
    returnFormat: Optional[AttributesRestSearchReturnFormat] = None


class AttributeRestSearchListItem(ExtendedAttribute):
    Event: Optional[Event] = None
    Object: Optional[Object] = None
    Tag: Optional[Sequence[Tag]] = None


class AttributeRestSearchList(RootModel[Sequence[AttributeRestSearchListItem]]):
    root: Sequence[AttributeRestSearchListItem]


class DateIntervalRestSearchFilter(RootModel[Sequence[str]]):
    root: Annotated[Sequence[str], Field(ge=2, le=2)]
    """
    Interval described by two dates
    """


class ExcludeLocalTagsRestSearchFilter(RootModel[Optional[bool]]):
    root: Optional[bool] = None
    """
    Exclude local tags from the export
    """
