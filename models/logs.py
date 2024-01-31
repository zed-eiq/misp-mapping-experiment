from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr, Field
from typing_extensions import Annotated

from models.common import (
    MispID,
    ModelName,
)


class LogActionType(str, Enum):
    ACCEPT = "accept"
    ACCEPT_DELEGATION = "accept_delegation"
    ACCEPT_REGISTRATIONS = "acceptRegistrations"
    ADD = "add"
    ADMIN_EMAIL = "admin_email"
    ATTACH_TAGS = "attachTags"
    AUTH = "auth"
    AUTH_FAIL = "auth_fail"
    BLOCKLISTED = "blocklisted"
    CAPTURE_RELATIONS = "captureRelations"
    CHANGE_PW = "change_pw"
    DELETE = "delete"
    DISABLE = "disable"
    DISCARD = "discard"
    DISCARD_REGISTRATIONS = "discardRegistrations"
    EDIT = "edit"
    EMAIL = "email"
    ENABLE = "enable"
    ENRICHMENT = "enrichment"
    ERROR = "error"
    EXPORT = "export"
    FETCH_EVENT = "fetchEvent"
    FILE_UPLOAD = "file_upload"
    GALAXY = "galaxy"
    INCLUDE_FORMULA = "include_formula"
    LOGIN = "login"
    LOGIN_FAIL = "login_fail"
    LOGOUT = "logout"
    MERGE = "merge"
    PRUNE_UPDATE_LOGS = "pruneUpdateLogs"
    PUBLISH = "publish"
    PUBLISH_SIGHTINGS = "publish_sightings"
    PUBLISH_ALERT = "publish alert"
    PULL = "pull"
    PURGE_EVENTS = "purge_events"
    PUSH = "push"
    REGISTRATION = "registration"
    REGISTRATION_ERROR = "registration_error"
    REMOVE_DEAD_WORKERS = "remove_dead_workers"
    REQUEST = "request"
    REQUEST_DELEGATION = "request_delegation"
    RESET_AUTH_KEY = "reset_auth_key"
    SEND_MAIL = "send_mail"
    SECURITY = "security"
    SERVER_SETTINGS_EDIT = "serverSettingsEdit"
    TAG = "tag"
    UNDELETE = "undelete"
    UPDATE = "update"
    UPDATE_DATABASE = "update_database"
    UPDATE_DB_WORKER = "update_db_worker"
    UPGRADE_24 = "upgrade_24"
    UPLOAD_SAMPLE = "upload_sample"
    VERSION_WARNING = "version_warning"
    WARNING = "warning"
    WIPE_DEFAULT = "wipe_default"


class Log(BaseModel):
    id: MispID
    title: Annotated[
        Optional[str],
        Field(None, examples=["Attribute (448272) from Event (1): Other/text foo"]),
    ]
    created: Optional[datetime] = None
    model: Optional[ModelName] = None
    model_id: MispID
    action: Optional[LogActionType] = None
    user_id: MispID
    change: Annotated[Optional[str], Field(None, examples=["name () => (ORGNAME)"])]
    email: Optional[EmailStr] = None
    org: Annotated[Optional[str], Field(None, examples=["ORGNAME"], max_length=255)]
    description: Annotated[
        Optional[str],
        Field(
            None, examples=['Organisation "ORGNAME" (1) added by User "SYSTEM" (0).']
        ),
    ]
    ip: Annotated[Optional[str], Field(None, examples=["10.0.0.10"])]
