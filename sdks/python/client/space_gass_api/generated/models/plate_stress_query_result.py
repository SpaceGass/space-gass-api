from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .plate_stress import PlateStress
    from .query_warnings import QueryWarnings

@dataclass
class PlateStressQueryResult(Parsable):
    """
    Wrapper for analysis query results.Contains the result data plus optional warnings about requested cases or modesthat produced no results (i.e. were not analysed).
    """
    # The query result rows.
    results: Optional[list[PlateStress]] = None
    # Warnings returned when some requested load cases or modes did not have analysisresults in the response. (Filter Ids that don't exist in the model are rejectedup-front with HTTP 400 by the controller — they never reach this DTO.)`loadCasesNotAnalyzed` is an SG list-format string that can be pasted straightinto `POST /job/analysis/run`'s `loadCases` field to re-run only thosecases. `modesNotAnalyzed` is a per-case list — each analysed case can computea different number of modes, so the warning is keyed by case rather than flattened.
    warnings: Optional[QueryWarnings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlateStressQueryResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlateStressQueryResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlateStressQueryResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .plate_stress import PlateStress
        from .query_warnings import QueryWarnings

        from .plate_stress import PlateStress
        from .query_warnings import QueryWarnings

        fields: dict[str, Callable[[Any], None]] = {
            "results": lambda n : setattr(self, 'results', n.get_collection_of_object_values(PlateStress)),
            "warnings": lambda n : setattr(self, 'warnings', n.get_object_value(QueryWarnings)),
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
        writer.write_collection_of_object_values("results", self.results)
        writer.write_object_value("warnings", self.warnings)
    

