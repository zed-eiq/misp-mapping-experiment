from __future__ import annotations

from collections.abc import Sequence
from enum import Enum
from typing import Optional, Union, Mapping, Any
from uuid import UUID

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from common import (
    MispID,
    AttributeType,
)


class DecayingModelParameters(BaseModel):
    lifetime: Annotated[Optional[float], Field(None, examples=[3])]
    decay_speed: Annotated[Optional[float], Field(None, examples=[2.3])]
    threshold: Annotated[Optional[float], Field(None, examples=[30])]
    default_base_score: Annotated[Optional[float], Field(None, examples=[80])]
    base_score_config: Annotated[
        Optional[Mapping[str, Any]],
        Field(
            None,
            examples=[
                {
                    "estimative-language:confidence-in-analytic-judgment": 0.25,
                    "estimative-language:likelihood-probability": 0.25,
                    "phishing:psychological-acceptability": 0.25,
                    "phishing:state": 0.2,
                }
            ],
        ),
    ]


class DecayingModel(BaseModel):
    id: MispID
    name: Annotated[
        Optional[str], Field(None, examples=["Phishing model"], max_length=255)
    ]


class Formula(str, Enum):
    POLYNOMIAL = "Polynomial"


class FullDecayingModel(BaseModel):
    id: MispID
    uuid: Optional[UUID]
    name: Annotated[
        Optional[str], Field(None, examples=["Phishing model"], max_length=255)
    ]
    description: Annotated[
        Optional[str],
        Field(
            None,
            examples=["Simple model to rapidly decay phishing website."],
            max_length=65535,
        ),
    ]
    parameters: Optional[DecayingModelParameters] = None
    attribute_types: Optional[Sequence[AttributeType]] = None
    org_id: MispID
    enabled: Optional[bool] = None
    all_orgs: Optional[bool] = None
    ref: Optional[Sequence[str]] = None
    formula: Optional[Formula] = None
    version: Annotated[Optional[str], Field(None, examples=["2"])]
    default: Optional[bool] = None
    isEditable: Optional[bool] = None


class DecayScore(BaseModel):
    score: Annotated[Optional[float], Field(None, examples=[10.5])]
    base_score: Annotated[Optional[float], Field(None, examples=[80])]
    decayed: Optional[bool] = None
    DecayingModel: Optional[Union[DecayingModel, FullDecayingModel]] = None
