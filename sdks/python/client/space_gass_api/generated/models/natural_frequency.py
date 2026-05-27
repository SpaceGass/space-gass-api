from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class NaturalFrequency(Parsable):
    """
    Dynamic natural frequency result (FileId 218).
    """
    # Frequency convergence tolerance.
    frequency_tolerance: Optional[float] = None
    # Number of iterations to converge.
    iterations: Optional[int] = None
    # Load case ID.
    load_case: Optional[int] = None
    # Mass participation factor in X direction.
    mass_part_x: Optional[float] = None
    # Mass participation factor in Y direction.
    mass_part_y: Optional[float] = None
    # Mass participation factor in Z direction.
    mass_part_z: Optional[float] = None
    # Mode number.
    mode: Optional[int] = None
    # Natural frequency. Unit: Hz.
    natural_frequency: Optional[float] = None
    # Natural period. Unit: seconds.
    natural_period: Optional[float] = None
    # Analysis engine warning message (empty if none).
    warning: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NaturalFrequency:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NaturalFrequency
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NaturalFrequency()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "frequencyTolerance": lambda n : setattr(self, 'frequency_tolerance', n.get_float_value()),
            "iterations": lambda n : setattr(self, 'iterations', n.get_int_value()),
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "massPartX": lambda n : setattr(self, 'mass_part_x', n.get_float_value()),
            "massPartY": lambda n : setattr(self, 'mass_part_y', n.get_float_value()),
            "massPartZ": lambda n : setattr(self, 'mass_part_z', n.get_float_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_int_value()),
            "naturalFrequency": lambda n : setattr(self, 'natural_frequency', n.get_float_value()),
            "naturalPeriod": lambda n : setattr(self, 'natural_period', n.get_float_value()),
            "warning": lambda n : setattr(self, 'warning', n.get_str_value()),
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
        writer.write_float_value("frequencyTolerance", self.frequency_tolerance)
        writer.write_int_value("iterations", self.iterations)
        writer.write_int_value("loadCase", self.load_case)
        writer.write_float_value("massPartX", self.mass_part_x)
        writer.write_float_value("massPartY", self.mass_part_y)
        writer.write_float_value("massPartZ", self.mass_part_z)
        writer.write_int_value("mode", self.mode)
        writer.write_float_value("naturalFrequency", self.natural_frequency)
        writer.write_float_value("naturalPeriod", self.natural_period)
        writer.write_str_value("warning", self.warning)
    

