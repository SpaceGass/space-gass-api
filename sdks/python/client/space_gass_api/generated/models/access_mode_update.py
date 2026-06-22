from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_mode import AccessMode

@dataclass
class AccessModeUpdate(Parsable):
    """
    Request body for `POST /service/access-mode`.
    """
    # Current operational mode of the API.
    access_mode: Optional[AccessMode] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessModeUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessModeUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessModeUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_mode import AccessMode

        from .access_mode import AccessMode

        fields: dict[str, Callable[[Any], None]] = {
            "accessMode": lambda n : setattr(self, 'access_mode', n.get_enum_value(AccessMode)),
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
    

