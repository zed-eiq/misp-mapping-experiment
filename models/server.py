from __future__ import annotations

from typing import Mapping, Sequence
from enum import Enum
from typing import Any, Optional, Union
from uuid import UUID

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Annotated

from models.common import MispID


class Position(BaseModel):
    x: Annotated[Optional[str], Field(None, examples=["0"], pattern="^\\d+$")]
    y: Annotated[Optional[str], Field(None, examples=["0"], pattern="^\\d+$")]
    width: Annotated[Optional[str], Field(None, examples=["2"], pattern="^\\d+$")]
    height: Annotated[Optional[str], Field(None, examples=["2"], pattern="^\\d+$")]


class DashboardUserSetting(BaseModel):
    widget: Annotated[Optional[str], Field(None, examples=["MispStatusWidget"])]
    position: Optional[Position] = None


class PublishAlertFilterUserSetting(BaseModel):
    pass


class HomepageUserSetting(BaseModel):
    path: Annotated[Optional[str], Field(None, examples=["/events/index"])]


class DefaultRestSearchParametersUserSetting(BaseModel):
    pass


class TagNumbericalValueOverrideUserSetting(BaseModel):
    pass


class UserSettingName(str, Enum):
    PUBLISH_ALERT_FILTER = "publish_alert_filter"
    DASHBOARD_ACCESS = "dashboard_access"
    DASHBOARD = "dashboard"
    HOMEPAGE = "homepage"
    DEFAULT_RESTSEARCH_PARAMETERS = "default_restsearch_parameters"
    TAG_NUMERICAL_VALUE_OVERRIDE = "tag_numerical_value_override"
    EVENT_INDEX_HIDE_COLUMNS = "event_index_hide_columns"


class ViewUserSettings(BaseModel):
    publish_alert_filter: Optional[PublishAlertFilterUserSetting] = None
    dashboard_access: Optional[bool] = None
    dashboard: Optional[Sequence[DashboardUserSetting]] = None
    homepage: Optional[HomepageUserSetting] = None
    default_restsearch_parameters: Optional[DefaultRestSearchParametersUserSetting] = (
        None
    )
    tag_numerical_value_override: Optional[TagNumbericalValueOverrideUserSetting] = None
    event_index_hide_columns: Optional[Sequence[str]] = None


class ChangePw(str, Enum):
    FIELD_0 = "0"
    FIELD_1 = "1"


class PhpServerSetting(BaseModel):
    explanation: Annotated[
        Optional[str],
        Field(
            None,
            examples=[
                "The maximum duration that a script can run (does not affect the background workers). A too low number will break long running scripts like comprehensive API exports"
            ],
        ),
    ]
    recommended: Optional[Union[int, str]] = None
    unit: Annotated[Optional[str], Field(None, examples=["seconds"])]
    value: Optional[Union[int, str]] = None


class ServerPackageVersion(BaseModel):
    version: Annotated[Optional[str], Field(None, examples=["1.2.0.11"])]
    expected: Annotated[Optional[str], Field(None, examples=[">1.2.0.9"])]
    status: Annotated[Optional[int], Field(None, examples=[1], ge=0)]


class DatabaseTableDiagnostics(BaseModel):
    used: Annotated[Optional[str], Field(None, examples=["207.63MB"])]
    reclaimable: Annotated[Optional[str], Field(None, examples=["5MB"])]
    table: Annotated[Optional[str], Field(None, examples=["attributes"])]


class Type(str, Enum):
    STRING = "string"
    BOOLEAN = "boolean"
    NUMERIC = "numeric"


class MispSetting(BaseModel):
    level: Annotated[Optional[int], Field(None, examples=[0])]
    value: Optional[Union[str, bool, float]] = None
    errorMessage: Annotated[
        Optional[str],
        Field(
            None,
            examples=[
                "The currently set baseurl does not match the URL"
                " through which you have accessed the page. "
                " Disregard this if you are accessing the page"
                " via an alternate URL (for example via IP address)."
            ],
        ),
    ]
    test: Optional[Union[str, bool]] = None
    type: Annotated[Optional[Type], Field(None, examples=["string"])]
    null: Optional[bool] = None
    subGroup: Annotated[Optional[str], Field(None, examples=["Enrichment"])]
    cli_only: Annotated[Optional[int], Field(None, examples=[1])]
    redacted: Optional[bool] = None
    optionsSource: Optional[Mapping[str, Any]] = None
    afterHook: Annotated[Optional[str], Field(None, examples=["cleanCacheFiles"])]
    error: Annotated[Optional[int], Field(None, examples=[1])]
    tab: Annotated[Optional[str], Field(None, examples=["MISP"])]
    setting: Annotated[Optional[str], Field(None, examples=["MISP.baseurl"])]
    options: Optional[
        Union[Mapping[str, Any], str, Sequence[str], Sequence[Mapping[str, Any]]]
    ] = None


class Worker(BaseModel):
    pid: Annotated[Optional[int], Field(None, examples=[1233])]
    user: Annotated[Optional[str], Field(None, examples=["www-data"])]
    alive: Optional[bool] = None
    correct_user: Optional[bool] = None
    ok: Optional[bool] = None


class WorkersStatus(BaseModel):
    ok: Optional[bool] = None
    workers: Optional[Sequence[Worker]] = None
    jobCount: Annotated[Optional[int], Field(None, examples=[0])]


class UpdateServerResultItem(BaseModel):
    input: Annotated[
        Optional[str],
        Field(
            None,
            examples=[
                "cd $(git rev-parse --show-toplevel) && git checkout app/composer.json 2>&1"
            ],
        ),
    ]
    output: Optional[Sequence[str]] = None
    status: Annotated[Optional[int], Field(None, examples=[0])]


class FeedSourceFormat(str, Enum):
    FIELD_1 = "1"
    CSV = "csv"
    FREETEXT = "freetext"
    MISP = "misp"


class FeedInputSource(str, Enum):
    LOCAL = "local"
    NETWORK = "network"


class UserSetting(BaseModel):
    id: MispID
    setting: Optional[UserSettingName] = None
    value: Optional[
        Union[
            DashboardUserSetting,
            PublishAlertFilterUserSetting,
            HomepageUserSetting,
            DefaultRestSearchParametersUserSetting,
            TagNumbericalValueOverrideUserSetting,
            bool,
            Sequence[str],
        ]
    ] = None
    user_id: MispID
    timestamp: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]


class SortSearchField(RootModel[Optional[str]]):
    root: Annotated[Optional[str], Field(None, examples=["timestamp"])] = None
    """
    Field to be used to sort the result
    """


class DirectionSearchField(str, Enum):
    ASC = "asc"
    DESC = "desc"


class ApiError(BaseModel):
    name: str
    message: str
    url: Annotated[str, Field(examples=["/attributes"])]


class UnauthorizedApiError(BaseModel):
    name: Annotated[
        str,
        Field(
            examples=[
                "Authentication failed. Please make sure you pass the API key of an API enabled user along in the Authorization header."
            ]
        ),
    ]
    message: Annotated[
        str,
        Field(
            examples=[
                "Authentication failed. Please make sure you pass the API key of an API enabled user along in the Authorization header."
            ]
        ),
    ]
    url: Annotated[str, Field(examples=["/attributes"])]


class NotFoundApiError(BaseModel):
    name: Annotated[str, Field(examples=["Invalid attribute"])]
    message: Annotated[str, Field(examples=["Invalid attribute"])]
    url: Annotated[str, Field(examples=["/attributes/1234"])]


class NotFoundUserTotpDeleteError(BaseModel):
    name: Annotated[str, Field(examples=["Invalid user"])]
    message: Annotated[str, Field(examples=["Invalid user"])]
    url: Annotated[str, Field(examples=["/users/totp_delete/1"])]


class AuthKey(BaseModel):
    id: MispID
    uuid: Optional[UUID]
    authkey_start: Annotated[Optional[str], Field(None, max_length=4)]
    authkey_end: Annotated[Optional[str], Field(None, max_length=4)]
    created: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]
    expiration: Annotated[Optional[str], Field(None, examples=["1970-01-01 00:00:00"])]
    read_only: Optional[bool] = None
    user_id: MispID
    comment: Optional[str] = None
    allowed_ips: Optional[Sequence[str]] = None
    last_used: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$|^$")
    ]
