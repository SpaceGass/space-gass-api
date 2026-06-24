from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .moving_load_combination import MovingLoadCombination
    from .moving_load_scenario_load import MovingLoadScenarioLoad

@dataclass
class MovingLoadScenario(Parsable):
    """
    A named moving-load scenario. The scenario header carries its name, include flag,starting load case, and time interval. Its load rows and combination rows are nestedcollections, hydrated inline only when `expand=All`.
    """
    # The scenario's combination rows. Populated only when `expand=All`; otherwise omitted.
    combinations: Optional[list[MovingLoadCombination]] = None
    # Whether the scenario has any combination rows.
    has_combinations: Optional[bool] = None
    # Whether the scenario has any load rows.
    has_loads: Optional[bool] = None
    # The item Id.
    id: Optional[int] = None
    # Whether this scenario is included when load cases are generated.
    include: Optional[bool] = None
    # The scenario's load rows. Populated only when `expand=All`; otherwise omitted.
    loads: Optional[list[MovingLoadScenarioLoad]] = None
    # The scenario name. Unique across all scenarios.
    name: Optional[str] = None
    # The first load case number generated for this scenario.
    starting_load_case: Optional[int] = None
    # Time between generated snapshots as a vehicle/pressure travels.
    time_interval: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MovingLoadScenario:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MovingLoadScenario
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MovingLoadScenario()
    
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
            "hasCombinations": lambda n : setattr(self, 'has_combinations', n.get_bool_value()),
            "hasLoads": lambda n : setattr(self, 'has_loads', n.get_bool_value()),
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
        writer.write_bool_value("hasCombinations", self.has_combinations)
        writer.write_bool_value("hasLoads", self.has_loads)
        writer.write_int_value("id", self.id)
        writer.write_bool_value("include", self.include)
        writer.write_collection_of_object_values("loads", self.loads)
        writer.write_str_value("name", self.name)
        writer.write_int_value("startingLoadCase", self.starting_load_case)
        writer.write_float_value("timeInterval", self.time_interval)
    

