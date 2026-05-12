from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ConvergenceEntry(Parsable):
    """
    A convergence result from a non-linear analysis iteration.
    """
    # Sequential iteration number (1-based)
    iteration: Optional[int] = None
    # Convergence percentage achieved at this iteration (e.g., 98.177)
    percentage: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConvergenceEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConvergenceEntry
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConvergenceEntry()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "iteration": lambda n : setattr(self, 'iteration', n.get_int_value()),
            "percentage": lambda n : setattr(self, 'percentage', n.get_float_value()),
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
        writer.write_int_value("iteration", self.iteration)
        writer.write_float_value("percentage", self.percentage)
    

