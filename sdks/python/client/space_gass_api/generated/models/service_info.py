from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ServiceInfo(Parsable):
    """
    Service information including API path and SPACE GASS version.
    """
    # The API base URL (e.g. https://localhost:34560/api).
    api_path: Optional[str] = None
    # SPACE GASS version number in format "X.XX.XXXX (ProgramType)"(e.g. "15.2.100 (Commercial)").
    space_gass_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServiceInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServiceInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServiceInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "apiPath": lambda n : setattr(self, 'api_path', n.get_str_value()),
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
        writer.write_str_value("spaceGassVersion", self.space_gass_version)
    

