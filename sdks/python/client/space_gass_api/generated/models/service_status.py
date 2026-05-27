from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ServiceStatus(Parsable):
    """
    Service status — always-reachable diagnostic endpoint that returnsthe API path, SPACE GASS version, current API mode, and registration/ licence presence. Replaces the previous `ServiceInfoDto`.
    """
    # The API base URL (e.g. https://localhost:34560/api).
    api_path: Optional[str] = None
    # True when the API holds the API module licence (Tier 1) — i.e.the session is active and the seat is checked out.
    is_licensed: Optional[bool] = None
    # True when this machine has a SPACE GASS registration the API can use(TitanCloud or Titan LM).
    is_registered: Optional[bool] = None
    # Current API mode. `"readwrite"` means writes and modulecheckout are allowed; `"readonly"` means no modules are heldand only reads + job lifecycle operations are accepted.
    mode: Optional[str] = None
    # Pending mode transition, set when a switch was requested butcannot be committed until the current job closes. Values:`"readonly"`, `"readwrite"`, or `null`.
    pending: Optional[str] = None
    # SPACE GASS version number in format "X.XX.XXXX (ProgramType)"(e.g. "15.2.100 (Commercial)").
    space_gass_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServiceStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServiceStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServiceStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "apiPath": lambda n : setattr(self, 'api_path', n.get_str_value()),
            "isLicensed": lambda n : setattr(self, 'is_licensed', n.get_bool_value()),
            "isRegistered": lambda n : setattr(self, 'is_registered', n.get_bool_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_str_value()),
            "pending": lambda n : setattr(self, 'pending', n.get_str_value()),
            "spaceGassVersion": lambda n : setattr(self, 'space_gass_version', n.get_str_value()),
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
        writer.write_str_value("apiPath", self.api_path)
        writer.write_bool_value("isLicensed", self.is_licensed)
        writer.write_bool_value("isRegistered", self.is_registered)
        writer.write_str_value("mode", self.mode)
        writer.write_str_value("pending", self.pending)
        writer.write_str_value("spaceGassVersion", self.space_gass_version)
    

