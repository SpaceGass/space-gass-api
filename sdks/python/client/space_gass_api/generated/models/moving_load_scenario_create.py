from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .moving_load_combination import MovingLoadCombination
    from .moving_load_scenario_load import MovingLoadScenarioLoad

@dataclass
class MovingLoadScenarioCreate(Parsable):
    """
    Creates a new moving-load scenario. Load and combination rows may be supplied inline (createdatomically with the scenario) or omitted and set later via`PUT moving-loads/scenarios/{id}/loads` / `.../combinations`.
    """
    # The scenario's combination rows. Optional — supply inline, or omit and set them later via `PUT .../{id}/combinations`.
    combinations: Optional[list[MovingLoadCombination]] = None
    # The Id to assign to the new item.
    id: Optional[int] = None
    # Whether this scenario is included when load cases are generated.
    include: Optional[bool] = None
    # The scenario's load rows, in order. Optional — supply to create the scenario and its loads in one call; omit to set them later via `PUT .../{id}/loads`.
    loads: Optional[list[MovingLoadScenarioLoad]] = None
    # The scenario name. Must be unique across all scenarios.
    name: Optional[str] = None
    # The first load case number generated for this scenario.
    starting_load_case: Optional[int] = None
    # Time between generated snapshots.
    time_interval: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MovingLoadScenarioCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MovingLoadScenarioCreate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MovingLoadScenarioCreate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .moving_load_combination import MovingLoadCombination
        from .moving_load_scenario_load import MovingLoadScenarioLoad

        from .moving_load_combination import MovingLoadCombination
        from .moving_load_scenario_load import MovingLoadScenarioLoad

        fields: dict[str, Callable[[Any], None]] = {
            "combinations": lambda n : setattr(self, 'combinations', n.get_collection_of_object_values(MovingLoadCombination)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "include": lambda n : setattr(self, 'include', n.get_bool_value()),
            "loads": lambda n : setattr(self, 'loads', n.get_collection_of_object_values(MovingLoadScenarioLoad)),
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
        writer.write_collection_of_object_values("combinations", self.combinations)
        writer.write_int_value("id", self.id)
        writer.write_bool_value("include", self.include)
        writer.write_collection_of_object_values("loads", self.loads)
        writer.write_str_value("name", self.name)
        writer.write_int_value("startingLoadCase", self.starting_load_case)
        writer.write_float_value("timeInterval", self.time_interval)
    

