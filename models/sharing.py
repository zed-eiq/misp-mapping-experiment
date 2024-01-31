from __future__ import annotations

from datetime import datetime
from typing import Optional
from typing import Sequence
from uuid import UUID

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Annotated

from models.common import (
    MispID,
)


class Role(BaseModel):
    id: Annotated[
        Optional[str], Field(None, examples=["3"], max_length=10, pattern="^\\d+$")
    ]
    name: Annotated[Optional[str], Field(None, examples=["ORGNAME"], max_length=255)]
    perm_add: Optional[bool] = None
    perm_modify: Optional[bool] = None
    perm_modify_org: Optional[bool] = None
    perm_publish: Optional[bool] = None
    perm_delegate: Optional[bool] = None
    perm_sync: Optional[bool] = None
    perm_admin: Optional[bool] = None
    perm_audit: Optional[bool] = None
    perm_auth: Optional[bool] = None
    perm_site_admin: Optional[bool] = None
    perm_regexp_access: Optional[bool] = None
    perm_tagger: Optional[bool] = None
    perm_template: Optional[bool] = None
    perm_sharing_group: Optional[bool] = None
    perm_tag_editor: Optional[bool] = None
    perm_sighting: Optional[bool] = None
    perm_object_template: Optional[bool] = None
    perm_publish_zmq: Optional[bool] = None
    perm_publish_kafka: Optional[bool] = None
    perm_decaying: Optional[bool] = None
    perm_galaxy_editor: Optional[bool] = None
    default_role: Optional[bool] = None
    memory_limit: Annotated[Optional[str], Field(None, pattern="^\\d+$|^$")]
    max_execution_time: Annotated[Optional[str], Field(None, pattern="^\\d+$|^$")]
    restricted_to_site_admin: Optional[bool] = None
    enforce_rate_limit: Optional[bool] = None
    rate_limit_count: Annotated[Optional[str], Field(None, pattern="^\\d+$")]
    permission: Annotated[Optional[str], Field(None, examples=["3"], pattern="^\\d+$")]
    permission_description: Annotated[Optional[str], Field(None, examples=["publish"])]


class SharingGroupServerId(RootModel[Optional[str]]):
    root: Annotated[
        Optional[str], Field(None, examples=["1"], max_length=10, pattern="^\\d+$|^$")
    ] = None


class Server1(BaseModel):
    id: MispID
    name: Annotated[
        Optional[str], Field(None, examples=["Phising Server"], max_length=255)
    ]


class SharingGroupServer(BaseModel):
    all_orgs: Optional[bool] = None
    server_id: MispID
    sharing_group_id: Annotated[
        Optional[str], Field(None, examples=["1"], max_length=10, pattern="^\\d+$|^$")
    ]
    Server: Optional[Server1] = None


class SlimSharingGroupNoId(BaseModel):
    uuid: Optional[UUID]
    name: Annotated[
        Optional[str], Field(None, examples=["Banking Sharing Group"], max_length=255)
    ]
    description: Annotated[
        Optional[str],
        Field(
            None, examples=["Banking Institutions of X Sharing Group"], max_length=65535
        ),
    ]
    releasability: Annotated[Optional[str], Field(None, max_length=65535)]
    local: Optional[bool] = None
    active: Optional[bool] = None
    org_count: Annotated[Optional[str], Field(None, examples=["6"], pattern="^\\d+$")]


class SlimSharingGroup(SlimSharingGroupNoId):
    id: Annotated[
        Optional[str], Field(None, examples=["1"], max_length=10, pattern="^\\d+$|^$")
    ]


class SharingGroupNoId(SlimSharingGroupNoId):
    organisation_uuid: Optional[UUID]
    org_id: MispID
    sync_user_id: MispID
    created: Optional[datetime] = None
    modified: Optional[str] = None
    roaming: Optional[bool] = None


class SharingGroup(SharingGroupNoId):
    id: Annotated[
        Optional[str], Field(None, examples=["1"], max_length=10, pattern="^\\d+$|^$")
    ]


class Organisation2(BaseModel):
    id: MispID
    name: Annotated[Optional[str], Field(None, examples=["ORGNAME"], max_length=255)]
    uuid: Optional[UUID]


class SharingGroupOrganisation(BaseModel):
    id: Annotated[
        Optional[str], Field(None, examples=["1"], max_length=10, pattern="^\\d+$|^$")
    ]
    sharing_group_id: Annotated[
        Optional[str], Field(None, examples=["1"], max_length=10, pattern="^\\d+$|^$")
    ]
    org_id: MispID
    extend: Optional[bool] = None
    Organisation: Optional[Organisation2] = None


class SharingGroupListItem(BaseModel):
    SharingGroup: Optional[SlimSharingGroup] = None
    Organisation: Optional[Organisation2] = None
    SharingGroupOrg: Optional[Sequence[SharingGroupOrganisation]] = None
    SharingGroupServer: Optional[Sequence[SharingGroupServer]] = None
    editable: Optional[bool] = None
    deletable: Optional[bool] = None
