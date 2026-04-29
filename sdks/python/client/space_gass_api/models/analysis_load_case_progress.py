from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AnalysisLoadCaseProgress(Parsable):
    """
    Load case progress information
    """
    # Total number of load cases
    count: Optional[int] = None
    # Current load case identifier
    id: Optional[int] = None
    # Current load case index (0-based)
    index: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalysisLoadCaseProgress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalysisLoadCaseProgress
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnalysisLoadCaseProgress()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "index": lambda n : setattr(self, 'index', n.get_int_value()),
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
        writer.write_int_value("count", self.count)
        writer.write_int_value("id", self.id)
        writer.write_int_value("index", self.index)
    

