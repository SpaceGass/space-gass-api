from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_mode import AccessMode

@dataclass
class AccessModeStatus(Parsable):
    """
    Service status — what the API can do right now: the current access mode,the access modes available to switch to, and any pending transition.
    """
    # Current operational mode of the API.
    access_mode: Optional[AccessMode] = None
    # The access modes the API can currently operate in — i.e. whichtargets `POST /service/access-mode` can be expected to accept.
    available_access_modes: Optional[list[AccessMode]] = None
    # Current operational mode of the API.
    pending_access_mode: Optional[AccessMode] = None
    # Human-readable explanation of the pending access-mode transition(e.g. "Job open — release on close").
    reason_if_access_mode_pending: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessModeStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessModeStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessModeStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_mode import AccessMode

        from .access_mode import AccessMode

        fields: dict[str, Callable[[Any], None]] = {
            "accessMode": lambda n : setattr(self, 'access_mode', n.get_enum_value(AccessMode)),
            "availableAccessModes": lambda n : setattr(self, 'available_access_modes', n.get_collection_of_enum_values(AccessMode)),
            "pendingAccessMode": lambda n : setattr(self, 'pending_access_mode', n.get_enum_value(AccessMode)),
            "reasonIfAccessModePending": lambda n : setattr(self, 'reason_if_access_mode_pending', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("accessMode", self.access_mode)
        writer.write_collection_of_enum_values("availableAccessModes", self.available_access_modes)
        writer.write_enum_value("pendingAccessMode", self.pending_access_mode)
        writer.write_str_value("reasonIfAccessModePending", self.reason_if_access_mode_pending)
    

