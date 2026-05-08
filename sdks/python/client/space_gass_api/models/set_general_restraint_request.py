from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SetGeneralRestraintRequest(Parsable):
    """
    Request body for `POST job/structure/node-restraints/set-general`.Provide a node Id to promote that node as the general restraint(demoting every other row); pass `null` to clear the flag from every node.
    """
    # The node to promote as the general restraint, or `null` to clear.
    node: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SetGeneralRestraintRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SetGeneralRestraintRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SetGeneralRestraintRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "node": lambda n : setattr(self, 'node', n.get_int_value()),
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
        writer.write_int_value("node", self.node)
    

