from __future__ import annotations

from typing import Sequence
from typing import Optional

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from models.common import (
    MispID,
)


class Taxonomy(BaseModel):
    id: MispID
    namespace: Annotated[Optional[str], Field(None, examples=["tlp"])]
    description: Annotated[
        Optional[str],
        Field(
            None,
            examples=[
                "Disclosure is not limited.  Sources may use TLP:WHITE when information carries minimal or no foreseeable risk of misuse, in accordance with applicable rules and procedures for public release. Subject to standard copyright rules, TLP:WHITE information may be distributed without restriction."
            ],
        ),
    ]
    version: Annotated[Optional[str], Field(None, examples=["5"], pattern="^\\d+$")]
    enabled: Optional[bool] = None
    exclusive: Optional[bool] = None
    required: Optional[bool] = None


class TaxonomyPredicate(BaseModel):
    id: MispID
    taxonomy_id: MispID
    value: Annotated[Optional[str], Field(None, examples=["white"])]
    expanded: Annotated[
        Optional[str],
        Field(
            None,
            examples=[
                "(TLP:WHITE) Information can be shared publicly in accordance with the law."
            ],
        ),
    ]
    colour: Annotated[Optional[str], Field(None, examples=["#ffffff"])]
    description: Annotated[
        Optional[str],
        Field(
            None,
            examples=[
                "Disclosure is not limited.  Sources may use TLP:WHITE when information carries minimal or no foreseeable risk of misuse, in accordance with applicable rules and procedures for public release. Subject to standard copyright rules, TLP:WHITE information may be distributed without restriction."
            ],
        ),
    ]
    exclusive: Optional[bool] = None
    numerical_value: Optional[int] = None


class TaxonomyPredicateExport(BaseModel):
    value: Annotated[Optional[str], Field(None, examples=["white"])]
    expanded: Annotated[
        Optional[str],
        Field(
            None,
            examples=[
                "(TLP:WHITE) Information can be shared publicly in accordance with the law."
            ],
        ),
    ]


class TaxonomyEntryExport(BaseModel):
    value: Annotated[Optional[str], Field(None, examples=["spam"])]
    expanded: Annotated[Optional[str], Field(None, examples=["spam"])]
    description: Annotated[
        Optional[str],
        Field(
            None,
            examples=[
                "Spam or ‘unsolicited bulk e-mail’, meaning that the recipient has not granted verifiable permission for the message to be sent and that the message is sent as part of a larger collection of messages, all having identical content."
            ],
        ),
    ]


class TaxonomyValueExport(BaseModel):
    predicate: Annotated[Optional[str], Field(None, examples=["white"])]
    entry: Optional[Sequence[TaxonomyEntryExport]] = None


class TaxonomyEntry(BaseModel):
    tag: Annotated[Optional[str], Field(None, examples=["tlp:white"], max_length=255)]
    expanded: Optional[str] = None
    description: Optional[str] = None
    exclusive_predicate: Optional[bool] = None
    existing_tag: Optional[bool] = None


class TagNoId(BaseModel):
    name: Annotated[Optional[str], Field(None, examples=["tlp:white"], max_length=255)]
    colour: Annotated[Optional[str], Field(None, examples=["#ffffff"], max_length=7)]
    exportable: Optional[bool] = None
    org_id: MispID
    user_id: MispID
    hide_tag: Optional[bool] = None
    numerical_value: Annotated[
        Optional[str], Field(None, examples=["12345"], pattern="^\\d+$")
    ]
    is_galaxy: Optional[bool] = None
    is_custom_galaxy: Optional[bool] = None
    inherited: Optional[int] = None


class Tag(TagNoId):
    id: MispID


class ExtendedTag(BaseModel):
    Tag: Optional[Tag] = None
    Taxonomy: Optional[Taxonomy] = None
    TaxonomyPredicate: Optional[TaxonomyPredicate] = None
