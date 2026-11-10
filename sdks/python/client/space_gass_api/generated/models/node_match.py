from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class NodeMatch(Parsable):
    """
    What is at one requested position.
    """
    # Id of the nearest node in the job closer than the tolerance, or null when there is none.
    node: Optional[int] = None
    # For a position with no node in the job: the index of the earlier position in this request itrepeats (closer than the tolerance), or null when it is the first at that location.
    same_as: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NodeMatch:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NodeMatch
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NodeMatch()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "node": lambda n : setattr(self, 'node', n.get_int_value()),
            "sameAs": lambda n : setattr(self, 'same_as', n.get_int_value()),
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
        writer.write_int_value("sameAs", self.same_as)
    

