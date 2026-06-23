from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MovingLoadCombination(Parsable):
    """
    One row of a scenario's "Combining with other Load Cases" table (the desktop ScenarioProperties dialog) — defines how the scenario's generated moving-load cases are combined withanother load case to produce combination cases. Distinct from a standalone combination loadcase (`job/loads/combination-load-cases`): these rows are owned by the scenario and setwholesale via `PUT moving-loads/scenarios/{id}/combinations`.
    """
    # The load case combined with the scenario's generated cases.
    combine_with_load_case: Optional[int] = None
    # Factor applied to SpaceGassApi.Models.Dtos.MovingLoads.MovingLoadCombinationDto.CombineWithLoadCase in the combination.
    load_case_factor: Optional[float] = None
    # Factor applied to the scenario's generated load cases in the combination.
    scenario_factor: Optional[float] = None
    # The first combination case number generated for this combination ("Starting Comb Case" in the dialog).
    starting_combination_case: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MovingLoadCombination:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MovingLoadCombination
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MovingLoadCombination()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "combineWithLoadCase": lambda n : setattr(self, 'combine_with_load_case', n.get_int_value()),
            "loadCaseFactor": lambda n : setattr(self, 'load_case_factor', n.get_float_value()),
            "scenarioFactor": lambda n : setattr(self, 'scenario_factor', n.get_float_value()),
            "startingCombinationCase": lambda n : setattr(self, 'starting_combination_case', n.get_int_value()),
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
        writer.write_int_value("combineWithLoadCase", self.combine_with_load_case)
        writer.write_float_value("loadCaseFactor", self.load_case_factor)
        writer.write_float_value("scenarioFactor", self.scenario_factor)
        writer.write_int_value("startingCombinationCase", self.starting_combination_case)
    

