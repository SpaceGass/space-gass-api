from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DefaultLibraries(Parsable):
    """
    The default library for each library type, as nominated in SPACE GASS(Preferences, Default Libraries).
    """
    # The default bolt library name (steel connection design), or null when none is recorded.
    bolts: Optional[str] = None
    # The default material library name, or null when none is available.
    materials: Optional[str] = None
    # The default plate library name (steel connection design plate sizes), or null when none is recorded.
    plates: Optional[str] = None
    # The default reinforcing bar library name (concrete design), or null when none is recorded.
    reinforcing_bars: Optional[str] = None
    # The default section library name, or null when none is available.
    sections: Optional[str] = None
    # The default spectral curve library name (dynamic response analysis), or null when none is recorded.
    spectral_curves: Optional[str] = None
    # The default vehicle (moving-load design vehicle) library name, or null when none is available.
    vehicles: Optional[str] = None
    # The default weld library name (steel connection design), or null when none is recorded.
    welds: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DefaultLibraries:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DefaultLibraries
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DefaultLibraries()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "bolts": lambda n : setattr(self, 'bolts', n.get_str_value()),
            "materials": lambda n : setattr(self, 'materials', n.get_str_value()),
            "plates": lambda n : setattr(self, 'plates', n.get_str_value()),
            "reinforcingBars": lambda n : setattr(self, 'reinforcing_bars', n.get_str_value()),
            "sections": lambda n : setattr(self, 'sections', n.get_str_value()),
            "spectralCurves": lambda n : setattr(self, 'spectral_curves', n.get_str_value()),
            "vehicles": lambda n : setattr(self, 'vehicles', n.get_str_value()),
            "welds": lambda n : setattr(self, 'welds', n.get_str_value()),
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
        writer.write_str_value("bolts", self.bolts)
        writer.write_str_value("materials", self.materials)
        writer.write_str_value("plates", self.plates)
        writer.write_str_value("reinforcingBars", self.reinforcing_bars)
        writer.write_str_value("sections", self.sections)
        writer.write_str_value("spectralCurves", self.spectral_curves)
        writer.write_str_value("vehicles", self.vehicles)
        writer.write_str_value("welds", self.welds)
    

