from __future__ import annotations

from collections.abc import Sequence
from typing import Optional, Union

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Annotated

from common import (
    MispID,
    DistributionLevelId,
    Timestamp,
)
from organisation import Organisation
from server import FeedInputSource, FeedSourceFormat


class ServerNoId(BaseModel):
    name: Annotated[
        Optional[str], Field(None, examples=["Phising Server"], max_length=255)
    ]
    url: Annotated[Optional[str], Field(None, examples=["https://misppriv.circl.lu"])]
    authkey: Annotated[
        Optional[str],
        Field(
            None,
            examples=["894c8d095180c7ea28789092e96ca6424199aa4f"],
            max_length=40,
            min_length=40,
        ),
    ]
    org_id: MispID
    push: Optional[bool] = None
    pull: Optional[bool] = None
    push_sightings: Optional[bool] = None
    push_galaxy_clusters: Optional[bool] = None
    pull_galaxy_clusters: Optional[bool] = None
    lastpulledid: MispID
    lastpushedid: MispID
    organization: Optional[str] = None
    remote_org_id: MispID
    publish_without_email: Optional[bool] = None
    unpublish_event: Optional[bool] = None
    self_signed: Optional[bool] = None
    pull_rules: Annotated[
        Optional[str],
        Field(
            None,
            examples=[
                '{"tags":{"OR":[],"NOT":[]},"orgs":{"OR":[],"NOT":[]},"url_params":""}'
            ],
        ),
    ]
    """
    Stringified JSON rules for pulling events from this server.
    """
    push_rules: Annotated[
        Optional[str],
        Field(None, examples=['{"tags":{"OR":[],"NOT":[]},"orgs":{"OR":[],"NOT":[]}}']),
    ]
    """
    Stringified JSON rules for pushing events from this server.
    """
    cert_file: Optional[str] = None
    """
    Base64 encoded certificate
    """
    client_cert_file: Optional[str] = None
    """
    Base64 encoded client certificate
    """
    internal: Optional[bool] = None
    skip_proxy: Optional[bool] = None
    caching_enabled: Optional[bool] = None
    priority: Annotated[
        Optional[str], Field(None, examples=["1"], max_length=10, pattern="^\\d+$")
    ]
    cache_timestamp: Optional[bool] = None


class Server(ServerNoId):
    id: MispID


class ServerListItem(BaseModel):
    Server: Optional[Server] = None
    Organisation: Optional[Organisation] = None
    RemoteOrg: Optional[Organisation] = None
    User: Optional[Sequence[User]] = None


class ServerList(RootModel[Sequence[ServerListItem]]):
    root: Sequence[ServerListItem]


class FeedNoId(BaseModel):
    name: Annotated[
        Optional[str], Field(None, examples=["CIRCL OSINT Feed"], max_length=255)
    ]
    provider: Annotated[Optional[str], Field(None, examples=["CIRCL"])]
    url: Annotated[
        Optional[str],
        Field(None, examples=["https://www.circl.lu/doc/misp/feed-osint"]),
    ]
    rules: Annotated[
        Optional[str],
        Field(
            None,
            examples=[
                '{"tags":{"OR":[],"NOT":[]},"orgs":{"OR":[],"NOT":[]},"url_params":""}'
            ],
        ),
    ]
    """
    Stringified JSON filter rules.
    """
    enabled: Optional[bool] = None
    distribution: Optional[DistributionLevelId] = None
    sharing_group_id: Annotated[
        Optional[str], Field(None, examples=["1"], max_length=10, pattern="^\\d+$|^$")
    ]
    tag_id: MispID
    default: Optional[bool] = None
    source_format: Optional[FeedSourceFormat] = None
    fixed_event: Optional[bool] = None
    """
    target_event option might be considered
    """
    delta_merge: Optional[bool] = None
    """
    Merge attributes (only add new attribute, remove revoked attributes)
    """
    event_id: MispID
    publish: Optional[bool] = None
    override_ids: Optional[bool] = None
    """
    The IDS flags will be set to Off for this feed
    """
    settings: Annotated[
        Optional[str],
        Field(
            None,
            examples=[
                '{"csv":{"value":"","delimiter":""},"common":{"excluderegex":""},"disable_correlation":"1"}'
            ],
        ),
    ]
    input_source: Optional[FeedInputSource] = None
    delete_local_file: Optional[bool] = None
    """
    The IDS flags will be set to Off for this feed
    """
    lookup_visible: Optional[bool] = None
    """
    The lookup will not be visible in the feed correlation
    """
    headers: Annotated[
        Optional[str],
        Field(None, examples=["X-Custom-Header-A: Foo\nX-Custom-Header-B: Bar\n"]),
    ]
    """
    Headers to be passed with the requests. All separated by 

    """
    caching_enabled: Optional[bool] = None
    """
    The feed is cached
    """
    force_to_ids: Optional[bool] = None
    """
    The IDS flags will be set to On for this feed
    """
    orgc_id: MispID
    cache_timestamp: Optional[Union[Timestamp, bool]] = None


class Feed(FeedNoId):
    id: Annotated[
        Optional[str], Field(None, examples=["3"], max_length=10, pattern="^\\d+$")
    ]
