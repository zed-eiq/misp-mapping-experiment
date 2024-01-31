from __future__ import annotations

from collections.abc import Sequence
from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Annotated


class Message(BaseModel):
    en: Annotated[
        Optional[str],
        Field(
            None,
            examples=[
                "This attribute is likely to contain personal data and"
                " the data subject is likely to be directly identifiable."
            ],
        ),
    ]


class Data(BaseModel):
    scope: Optional[Sequence[str]] = None
    field: Optional[Sequence[str]] = None
    value: Optional[Sequence[str]] = None
    tags: Annotated[Optional[Sequence[str]], Field(None, max_length=255)]
    message: Optional[Message] = None


class WarninglistId(RootModel[str]):
    root: Annotated[str, Field(examples=["3"], max_length=10, pattern="^\\d+$")]


class WarninglistEntry(BaseModel):
    id: Annotated[Optional[str], Field(None, examples=["1234"], pattern="^\\d+$")]
    value: Annotated[Optional[str], Field(None, examples=["10.128.0.0/24"])]
    warninglist_id: Annotated[
        Optional[str], Field(None, examples=["3"], max_length=10, pattern="^\\d+$")
    ]


class WarningListType(str, Enum):
    CIDR = "cidr"
    HOSTNAME = "hostname"
    SUBSTRING = "substring"
    STRING = "string"
    REGEX = "regex"


class Warninglist(BaseModel):
    id: Annotated[
        Optional[str], Field(None, examples=["3"], max_length=10, pattern="^\\d+$")
    ]
    name: Annotated[
        Optional[str],
        Field(None, examples=["List of known domains to know external IP"]),
    ]
    type: Annotated[Optional[WarningListType], Field(None, examples=["cidr"])]
    description: Optional[str] = None
    version: Annotated[Optional[str], Field(None, examples=["10"], pattern="^\\d+$")]
    enabled: Optional[bool] = None
    warninglist_entry_count: Annotated[
        Optional[str], Field(None, examples=["1234"], pattern="^\\d+$")
    ]
    valid_attributes: Annotated[
        Optional[str], Field(None, examples=["domain, hostname, domain|ip, uri, url"])
    ]
    """
    List of comma separated warninglist types.
    """
    WarninglistEntry: Optional[Sequence[WarninglistEntry]] = None


class WarninglistsIdFilter(RootModel[Union[WarninglistId, Sequence[WarninglistId]]]):
    root: Union[WarninglistId, Sequence[WarninglistId]]


class WarninglistsNameFilter(RootModel[Union[str, Sequence[str]]]):
    root: Union[str, Sequence[str]]


class NoticelistEntry(BaseModel):
    id: Annotated[Optional[str], Field(None, examples=["1234"], pattern="^\\d+$")]
    noticelist_id: Annotated[
        Optional[str], Field(None, examples=["3"], max_length=10, pattern="^\\d+$")
    ]
    data: Optional[Data] = None


class Noticelist(Warninglist):
    """
    List of comma separated warninglist types.
    """
    NoticelistEntry: Optional[Sequence[NoticelistEntry]] = None
