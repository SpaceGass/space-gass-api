from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class NodeMatchSummary(Parsable):
    """
    Counts of the match outcomes. `existing + new + repeated` is the number of positions.
    """
    # Positions with a node in the job (`node` is set).
    existing: Optional[int] = None
    # Positions that need a new node: no node in the job and not a repeat of an earlier position.
    new: Optional[int] = None
    # Positions that repeat an earlier position in the request (`sameAs` is set).
    repeated: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NodeMatchSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NodeMatchSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NodeMatchSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "existing": lambda n : setattr(self, 'existing', n.get_int_value()),
            "new": lambda n : setattr(self, 'new', n.get_int_value()),
            "repeated": lambda n : setattr(self, 'repeated', n.get_int_value()),
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
        writer.write_int_value("existing", self.existing)
        writer.write_int_value("new", self.new)
        writer.write_int_value("repeated", self.repeated)
    

