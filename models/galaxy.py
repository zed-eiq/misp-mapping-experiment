from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any, Optional, Union
from uuid import UUID

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Annotated

from common import MispID, DistributionLevelId
from organisation import Organisation


class GalaxyClusterVersion(RootModel[Optional[str]]):
    root: Annotated[Optional[str], Field(None, examples=["1"], max_length=255)] = None


class GalaxyElement(BaseModel):
    id: MispID
    galaxy_cluster_id: MispID
    key: Annotated[Optional[str], Field(None, examples=["categories"], max_length=255)]
    value: Annotated[
        Optional[str], Field(None, examples=["Military"], max_length=65535)
    ]


class GalaxyElementList(RootModel[Sequence[GalaxyElement]]):
    root: Sequence[GalaxyElement]


class GalaxyValueSearchFilter(RootModel[str]):
    root: Annotated[str, Field(examples=["botnet"])]
    """
    Text search term to find a matching galaxy name, namespace, description, kill_chain_order or uuid.
    """


class Galaxy(BaseModel):
    id: MispID
    uuid: Optional[UUID]
    name: Annotated[Optional[str], Field(None, examples=["Ransomware"], max_length=255)]
    type: Annotated[Optional[str], Field(None, examples=["ransomware"], max_length=255)]
    description: Annotated[
        Optional[str],
        Field(None, examples=["Ransomware galaxy based on ..."], max_length=65535),
    ]
    version: Annotated[Optional[str], Field(None, examples=["1"], max_length=255)]
    icon: Annotated[Optional[str], Field(None, examples=["globe"], max_length=255)]
    namespace: Annotated[Optional[str], Field(None, examples=["misp"], max_length=255)]
    kill_chain_order: Annotated[
        Optional[Mapping[str, Any]],
        Field(
            None,
            examples=[
                {
                    "fraud-tactics": [
                        "Initiation",
                        "Target Compromise",
                        "Perform Fraud",
                        "Obtain Fraudulent Assets",
                        "Assets Transfer",
                        "Monetisation",
                    ]
                }
            ],
        ),
    ]


class GalaxyClusterNoId(BaseModel):
    uuid: Optional[UUID]
    collection_uuid: Optional[UUID]
    type: Annotated[
        Optional[str],
        Field(
            None, examples=["mitre-enterprise-attack-attack-pattern"], max_length=255
        ),
    ]
    value: Annotated[
        Optional[str], Field(None, examples=["Brute Force - T1110"], max_length=65535)
    ]
    tag_name: Annotated[
        Optional[str], Field(None, examples=["tlp:white"], max_length=255)
    ]
    description: Annotated[
        Optional[str],
        Field(
            None,
            examples=[
                "Adversaries may use brute force techniques to attempt access to accounts when passwords are unknown or when password hashes are obtained..."
            ],
            max_length=65535,
        ),
    ]
    galaxy_id: MispID
    source: Annotated[
        Optional[str],
        Field(None, examples=["https://github.com/mitre/cti"], max_length=255),
    ]
    authors: Optional[Sequence[str]] = None
    version: Annotated[Optional[str], Field(None, examples=["1"], max_length=255)]
    distribution: Optional[DistributionLevelId] = None
    sharing_group_id: Annotated[
        Optional[str], Field(None, examples=["1"], max_length=10, pattern="^\\d+$|^$")
    ]
    org_id: MispID
    orgc_id: MispID
    default: Optional[bool] = None
    locked: Optional[bool] = None
    extends_uuid: Annotated[
        Optional[str],
        Field(None, examples=["c99506a6-1255-4b71-afa5-7b8ba48c3b1b"], max_length=36),
    ]
    extends_version: Annotated[
        Optional[str], Field(None, examples=["1"], max_length=255)
    ]
    published: Optional[bool] = None
    deleted: Optional[bool] = None
    GalaxyElement: Optional[Sequence[GalaxyElement]] = None


class GalaxyCluster(GalaxyClusterNoId):
    id: MispID


class ExtendedGalaxyCluster(GalaxyCluster):
    Galaxy: Optional[Galaxy] = None
    GalaxyClusterRelation: Optional[Sequence[GalaxyElement]] = None
    Org: Optional[Organisation] = None
    Orgc: Optional[Organisation] = None
    tag_count: Optional[int] = None
    tag_id: MispID


class ExtendedGalaxy(BaseModel):
    Galaxy: Optional[Galaxy] = None
    GalaxyCluster: Optional[Sequence[GalaxyCluster]] = None


class Value(BaseModel):
    description: Annotated[
        Optional[str],
        Field(
            None,
            examples=[
                "Adversaries may use brute force techniques to attempt access to accounts when passwords are unknown or when password hashes are obtained..."
            ],
            max_length=65535,
        ),
    ]
    uuid: Optional[UUID]
    value: Annotated[
        Optional[str], Field(None, examples=["Brute Force - T1110"], max_length=65535)
    ]
    extends_uuid: Annotated[
        Optional[str],
        Field(None, examples=["c99506a6-1255-4b71-afa5-7b8ba48c3b1b"], max_length=36),
    ]
    extends_Version: Annotated[
        Optional[str], Field(None, examples=["1"], max_length=255)
    ]
    meta: Annotated[
        Optional[Mapping[str, Any]],
        Field(
            None,
            examples=[
                [
                    {"categories": "botnet"},
                    {"refs": "http://example.com"},
                    {"aliases": ["malware", "win32", "windows"]},
                    {"topics": ["Windows", "Malware"]},
                ]
            ],
        ),
    ]
    """
    Each Galaxy element associated to this cluster represents a key-value property.
    """


class GalaxyMispFormat(BaseModel):
    name: Annotated[Optional[str], Field(None, examples=["Ransomware"], max_length=255)]
    type: Annotated[Optional[str], Field(None, examples=["ransomware"], max_length=255)]
    authors: Optional[Sequence[str]] = None
    version: Optional[Union[bool, GalaxyClusterVersion]] = None
    uuid: Optional[UUID]
    source: Annotated[
        Optional[str],
        Field(None, examples=["https://github.com/mitre/cti"], max_length=255),
    ]
    values: Optional[Sequence[Value]] = None


class Galaxy1(BaseModel):
    uuid: Optional[UUID]


class ImportGalaxyClusterItem(BaseModel):
    GalaxyCluster: Optional[GalaxyClusterNoId] = None
    Galaxy: Optional[Galaxy1] = None
