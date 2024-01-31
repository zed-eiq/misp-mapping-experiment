from __future__ import annotations

from enum import Enum
from typing import Optional, List
from typing import Sequence
from uuid import UUID

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from models.common import (
    MispID,
    DistributionLevelId,
)
from models.events import Event4


class ObjectNames(str, Enum):
    ACQUAINTANCE = 'Acquaintance'
    CHILD = 'Child'
    CO_RESIDENT = 'Co-resident'
    CO_WORKER = 'Co-worker'
    COLLEAGUE = 'Colleague'
    CONTACT = 'Contact'
    CRUSH = 'Crush'
    DATE = 'Date'
    FRIEND = 'Friend'
    KIN = 'Kin'
    ME = 'Me'
    MET = 'Met'
    MUSE = 'Muse'
    NEIGHBOR = 'Neighbor'
    PARENT = 'Parent'
    SIBLING = 'Sibling'
    SPOUSE = 'Spouse'
    SWEETHEART = 'Sweetheart'
    ABUSES = 'abuses'
    ACQUAINTANCE_OF = 'acquaintance-of'
    ADMINISTRATOR_OF = 'administrator-of'
    AFFECTED_BY = 'affected-by'
    AFFECTS = 'affects'
    AFFILIATED = 'affiliated'
    ALERTS = 'alerts'
    ALLEGED_FOUNDER_OF = 'alleged-founder-of'
    AMBIVALENT_OF = 'ambivalient-of'
    ANALYSED_WITH = 'analysed-with'
    ANNOTATES = 'annotates'
    ANTAGONIST_OF = 'antagonist-of'
    ASSIGNED = 'assigned'
    ASSOCIATED_WITH = 'associated-with'
    ATTACKING_OTHER_GROUP = 'attacking-other-group'
    ATTRIBUTED_TO = 'attributed-to'
    AUTHORED_BY = 'authored-by'
    AWARDED_TO = 'awarded-to'
    BASED_ON = 'based-on'
    BEACONS_TO = 'beacons-to'
    BELONGS_TO = 'belongs-to'
    BLOCKED_BY = 'blocked-by'
    BLOCKS = 'blocks'
    BUSINESS_RELATIONS = 'business-relations'
    CALLS = 'calls'
    CAUSED_BY = 'caused-by'
    CAUSES = 'causes'
    CHARACTERIZED_BY = 'characterized-by'
    CHARACTERIZES = 'characterizes'
    CHILD_OF = 'child-of'
    CLAIMED_BY = 'claimed-by'
    CLAIMS_TO_BE_THE_FOUNDER_OF = 'claims-to-be-the-founder-of'
    COMMUNICATES_WITH = 'communicates-with'
    COMPROMISED = 'compromised'
    CONNECTED_FROM = 'connected-from'
    CONNECTED_TO = 'connected-to'
    CONNECTS = 'connects'
    CONNECTS_TO = 'connects-to'
    CONSISTS = 'consists'
    CONTACT_FOR = 'contact-for'
    CONTAINED_BY = 'contained-by'
    CONTAINED_WITHIN = 'contained-within'
    CONTAINS = 'contains'
    CONTROLS = 'controls'
    COOPERATES_WITH = 'cooperates-with'
    COVER_TERM_FOR = 'cover-term-for'
    CREATED_BY = 'created-by'
    CREATES = 'creates'
    CREATOR_OF = 'creator-of'
    DELIVERED_BY = 'delivered-by'
    DELIVERS = 'delivers'
    DERIVED_FROM = 'derived-from'
    DESCRIBES = 'describes'
    DETECTED_AS = 'detected-as'
    DETECTED_BY = 'detected-by'
    DETECTS = 'detects'
    DEVELOPER_OF = 'developer-of'
    DIRECTS = 'directs'
    DISCLOSED_TO = 'disclosed-to'
    DOCUMENTS = 'documents'
    DOES_NOT_TARGET = 'does-not-target'
    DOWNLOADED = 'downloaded'
    DOWNLOADED_FROM = 'downloaded-from'
    DOWNLOADS = 'downloads'
    DOWNLOADS_FROM = 'downloads-from'
    DOXED_BY = 'doxed-by'
    DRIVES = 'drives'
    DROPPED = 'dropped'
    DROPPED_BY = 'dropped-by'
    DROPS = 'drops'
    DUPLICATE_OF = 'duplicate-of'
    ENEMY_OF = 'enemy-of'
    ERRORED_TO = 'errored-to'
    EXECUTED_BY = 'executed-by'
    EXECUTES = 'executes'
    EXFILTRATES_TO = 'exfiltrates-to'
    EXPLOITS = 'exploits'
    EXTENDS = 'extends'
    EXTRACTED_FROM = 'extracted-from'
    FOLLOWED_BY = 'followed-by'
    FORMER_MEMBER_OF = 'former-member-of'
    FOUND_IN = 'found-in'
    FOUND_ON = 'found-on'
    FRIEND_OF = 'friend-of'
    GENERATED = 'generated'
    GRANDCHILD_OF = 'grandchild-of'
    HAS_JOINED = 'has-joined'
    HAS_MET = 'has-met'
    HOSTED_BY = 'hosted-by'
    HOSTS = 'hosts'
    IDENTIFIES = 'identifies'
    IMPACTED_BY = 'impacted-by'
    IMPACTS = 'impacts'
    IMPERSONATES = 'impersonates'
    IMPLEMENTS = 'implements'
    INCLUDED_IN = 'included-in'
    INCLUDES = 'includes'
    INDICATED_BY = 'indicated-by'
    INDICATES = 'indicates'
    INITIATES = 'initiates'
    INJECTED_INTO = 'injected-into'
    INJECTS_INTO = 'injects-into'
    INSTANCE_OF = 'instance-of'
    INTERCEPTS = 'intercepts'
    INVOLVED_IN = 'involved-in'
    IS_A_TRANSLATION_OF = 'is-a-translation-of'
    IS_AUTHOR_OF = 'is-author-of'
    IS_IN_RELATION_WITH = 'is-in-relation-with'
    IS_NOT_TARGETED_BY = 'is-not-targeted-by'
    IS_TARGETED_BY = 'is-targeted-by'
    ISSUER_OF = 'issuer-of'
    KNOWN_AS = 'known-as'
    KNOWS = 'knows'
    LEAKED_BY = 'leaked-by'
    LEAKS = 'leaks'
    LED_TO = 'led-to'
    LEGAL_ADDRESS_OF = 'legal-address-of'
    LINKED_TO = 'linked-to'
    LOCATED = 'located'
    LOCATED_AT = 'located-at'
    MEMBER_OF = 'member-of'
    MENTIONS = 'mentions'
    MITIGATES = 'mitigates'
    NOT_RELEVANT_TO = 'not-relevant-to'
    OBSERVED = 'observed'
    OBSERVED_BY = 'observed-by'
    OFFICE_OF = 'office-of'
    OPERATOR_OF = 'operator-of'
    OVERLAPS = 'overlaps'
    OWES = 'owes'
    OWNER_OF = 'owner-of'
    OWNS = 'owns'
    PAID = 'paid'
    PARENT_OF = 'parent-of'
    PART_OF = 'part-of'
    PARTICIPATED_IN = 'participated-in'
    PERFORMED = 'performed'
    PERFORMED_BY = 'performed-by'
    PICTURE_OF = 'picture-of'
    PICTURED_BY = 'pictured-by'
    PRECEDED_BY = 'preceded-by'
    PRECEEDS = 'preceeds'
    PRIMARY_MEMBER_OF = 'primary-member-of'
    PROCESSED_BY = 'processed-by'
    PRODUCED = 'produced'
    PROPERTIES_QUERIED = 'properties-queried'
    PROPERTIES_QUERIED_BY = 'properties-queried-by'
    PROVIDE_SUPPORT_TO = 'provide-support-to'
    PUBLISHES_METHOD_FOR = 'publishes-method-for'
    QUERIED_FOR = 'queried-for'
    QUERY_RETURNED = 'query-returned'
    RANKED_WITH = 'ranked-with'
    RECOMMENDS_USE_OF = 'recommends-use-of'
    REDIRECTS_TO = 'redirects-to'
    REFERENCES = 'references'
    REGIONAL_BRANCH = 'regional-branch'
    REGISTERED = 'registered'
    REGISTERED_TO = 'registered-to'
    RELATED_TO = 'related-to'
    RELATES = 'relates'
    RELEASED = 'released'
    RELEASED_SOURCE_CODE = 'released-source-code'
    RELEVANT_TO = 'relevant-to'
    RENDERED_AS = 'rendered-as'
    REPRESENTS = 'represents'
    RESOLVED_TO = 'resolved-to'
    RESOLVES_TO = 'resolves-to'
    RESPONSIBLE_FOR = 'responsible-for'
    RETRIEVED_FROM = 'retrieved-from'
    REWRITE = 'rewrite'
    SAME_AS = 'same-as'
    SAMPLE_OF = 'sample-of'
    SCREENSHOT_OF = 'screenshot-of'
    SEEDED = 'seeded'
    SELLER_OF = 'seller-of'
    SELLER_ON = 'seller-on'
    SENDS = 'sends'
    SENDS_AS_BCC_TO = 'sends-as-bcc-to'
    SENDS_AS_CC_TO = 'sends-as-cc-to'
    SENDS_TO = 'sends-to'
    SERVES = 'serves'
    SHIPPING_ADDRESS_OF = 'shipping-address-of'
    SIBLING_OF = 'sibling-of'
    SIGNED_BY = 'signed-by'
    SIMILAR = 'similar'
    SPOOFER_OF = 'spoofer-of'
    SPOUSE_OF = 'spouse-of'
    SUB_DOMAIN_OF = 'sub-domain-of'
    SUBDOMAIN_OF = 'subdomain-of'
    SUBGROUP = 'subgroup'
    SUBMITTED = 'submitted'
    SUBMITTED_BY = 'submitted-by'
    SUCCESSOR_OF = 'successor-of'
    SUPERSEDES = 'supersedes'
    SUPRA_DOMAIN_OF = 'supra-domain-of'
    SUSPECTED_LINK = 'suspected-link'
    TARGETED_BY = 'targeted-by'
    TARGETS = 'targets'
    TRIGGERED_ON = 'triggered-on'
    TRIGGERS = 'triggers'
    TRYING_TO_OBTAIN_THE_EXPLOIT = 'trying-to-obtain-the-exploit'
    UPLOADS = 'uploads'
    USED_BY = 'used-by'
    USER_OF = 'user-of'
    USES = 'uses'
    USES_FOR_RECON = 'uses-for-recon'
    VARIANT_OF = 'variant-of'
    VISITED = 'visited'
    VULNERABILITY_OF = 'vulnerability-of'
    WITNESS_OF = 'witness-of'
    WORKS_FOR = 'works-for'
    WORKS_LIKE = 'works-like'
    WORKS_WITH = 'works-with'
    WRITES = 'writes'


class ObjectFormats(str, Enum):
    XFN = "XFN"
    ALFRED = "alfred"
    CERT_EU = "cert-eu"
    FOAF = "foaf"
    FOLLOWTHEMONEY = "followthemoney"
    HAXPAK = "haxpak"
    MISP = "misp"
    STIX11 = "stix-1.1"
    STIX20 = "stix-2.0"
    STIX21 = "stix-2.1"


class ObjectRelationshipType(BaseModel):
    # See object-relationship.json
    # or https://github.com/MISP/misp-objects/blob/main/relationships/definition.json
    name: ObjectNames
    oppposite: ObjectNames = None  # Name of relationship in reverse direction
    format: List[ObjectFormats]
    description: str


class Object(BaseModel):
    id: MispID
    name: Annotated[
        Optional[str], Field(None, examples=["ail-leak"], max_length=131071)
    ]
    meta_category: Annotated[Optional[str], Field(None, alias="meta-category")]
    description: Optional[str] = None
    template_uuid: Optional[UUID]
    template_version: Annotated[
        Optional[str], Field(None, examples=["1"], pattern="^\\d+$")
    ]
    event_id: MispID
    uuid: Optional[UUID]
    timestamp: Annotated[
        Optional[str], Field(None, examples=["1617875568"], pattern="^\\d+$")
    ]
    distribution: Optional[DistributionLevelId] = None
    sharing_group_id: Annotated[
        Optional[str], Field(None, examples=["1"], max_length=10, pattern="^\\d+$|^$")
    ]
    comment: Optional[str] = None
    deleted: Optional[bool] = None
    first_seen: Annotated[
        Optional[str], Field(None, examples=["1581984000000000"], pattern="^\\d+$|^$")
    ]
    last_seen: Annotated[
        Optional[str], Field(None, examples=["1581984000000000"], pattern="^\\d+$|^$")
    ]
    Attribute: Optional[Sequence[Attribute]] = None


class ExtendedObject(Object):
    Event: Optional[Event4] = None
