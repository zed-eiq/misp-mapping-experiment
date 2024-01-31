from __future__ import annotations

from typing import Sequence
from typing import Optional

from pydantic import AwareDatetime, BaseModel, EmailStr, Field, RootModel
from typing_extensions import Annotated

from models.common import (
    MispID,
)
from models.server import ChangePw, ViewUserSettings


class UserNoId(BaseModel):
    org_id: MispID
    server_id: MispID
    email: Optional[EmailStr] = None
    autoalert: Optional[bool] = None
    authkey: Annotated[
        Optional[str],
        Field(
            None,
            examples=["894c8d095180c7ea28789092e96ca6424199aa4f"],
            max_length=40,
            min_length=40,
        ),
    ]
    """
    API auth key used for the API, only set if MISP setting `Security.advanced_authkeys` is set to `false`.
    """
    invited_by: MispID
    gpgkey: Optional[str] = None
    certif_public: Optional[str] = None
    nids_sid: Annotated[
        Optional[str],
        Field(None, examples=["4000000"], max_length=10, pattern="^\\d+$"),
    ]
    termsaccepted: Optional[bool] = None
    newsread: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]
    role_id: Annotated[
        Optional[str], Field(None, examples=["3"], max_length=10, pattern="^\\d+$")
    ]
    change_pw: Optional[ChangePw] = None
    """
    Password change required.
    """
    contactalert: Optional[bool] = None
    disabled: Optional[bool] = None
    expiration: Optional[AwareDatetime] = None
    current_login: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]
    last_login: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]
    force_logout: Optional[bool] = None
    date_created: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]
    date_modified: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]


class User(UserNoId):
    id: MispID


class ExtendedUser(User):
    User: Optional[User] = None
    Role: Optional[Role] = None
    UserSetting: Optional[ViewUserSettings] = None


class Organisation1(BaseModel):
    id: MispID
    name: Annotated[Optional[str], Field(None, examples=["ORGNAME"], max_length=255)]


class UserListItem(BaseModel):
    User: Optional[User] = None
    Role: Optional[Role] = None
    Organisation: Optional[Organisation1] = None


class UserList(RootModel[Sequence[UserListItem]]):
    root: Sequence[UserListItem]
