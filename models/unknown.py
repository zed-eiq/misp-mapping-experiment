from __future__ import annotations

from typing import Mapping, Sequence
from typing import Any, Optional

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Annotated

from models.common import (
    AttributeType,
    AttributeCategory,
)


class AttributeStatisticsResponse(BaseModel):
    pass


class DescribeAttributeTypesResponse(BaseModel):
    sane_defaults: Annotated[
        Optional[Mapping[str, Any]],
        Field(
            None,
            examples=[
                {
                    "md5": {"default_category": "Payload delivery", "to_ids": 1},
                    "pdb": {"default_category": "Artifacts dropped", "to_ids": 0},
                }
            ],
        ),
    ]
    types: Optional[Sequence[AttributeType]] = None
    categories: Optional[Sequence[AttributeCategory]] = None
    category_type_mappings: Annotated[
        Optional[Mapping[str, Any]],
        Field(
            None,
            examples=[
                {
                    "Internal reference": ["text", "link", "comment", "other"],
                    "Antivirus detection": ["link", "comment", "text", "hex", "other"],
                }
            ],
        ),
    ]


class ObjectRelation(RootModel[str]):
    root: Annotated[str, Field(examples=["sensor"], max_length=255)]


class ObjectTemplateId(RootModel[str]):
    root: Annotated[str, Field(examples=["12345"], max_length=10, pattern="^\\d+$")]


class TagCollectionId(RootModel[str]):
    root: Annotated[str, Field(examples=["12345"], max_length=10, pattern="^\\d+$")]
