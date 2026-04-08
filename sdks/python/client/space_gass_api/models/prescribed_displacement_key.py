from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PrescribedDisplacementKey(Parsable):
    """
    Composite key object for bulk delete operations.
    """
    # The load case number.
    case: Optional[int] = None
    # The node number.
    node: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrescribedDisplacementKey:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrescribedDisplacementKey
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrescribedDisplacementKey()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "case": lambda n : setattr(self, 'case', n.get_int_value()),
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
        writer.write_int_value("case", self.case)
        writer.write_int_value("node", self.node)
    

