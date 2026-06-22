from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MovingLoadScenarioUpdate(Parsable):
    """
    Partial update for a moving-load scenario header. All properties are optional; omittedproperties keep their current value.
    """
    # The Id of the item to update.
    id: Optional[int] = None
    # Whether the scenario is included in generation. Omit to keep current.
    include: Optional[bool] = None
    # Replacement scenario name. Must remain unique. Omit to keep current.
    name: Optional[str] = None
    # The first generated load case number. Omit to keep current.
    starting_load_case: Optional[int] = None
    # Time between generated snapshots (seconds). Omit to keep current.
    time_interval: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MovingLoadScenarioUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MovingLoadScenarioUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MovingLoadScenarioUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "include": lambda n : setattr(self, 'include', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "startingLoadCase": lambda n : setattr(self, 'starting_load_case', n.get_int_value()),
            "timeInterval": lambda n : setattr(self, 'time_interval', n.get_float_value()),
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
        writer.write_int_value("id", self.id)
        writer.write_bool_value("include", self.include)
        writer.write_str_value("name", self.name)
        writer.write_int_value("startingLoadCase", self.starting_load_case)
        writer.write_float_value("timeInterval", self.time_interval)
    

