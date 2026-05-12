from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .case_modes_warning import CaseModesWarning

@dataclass
class QueryWarnings(Parsable):
    """
    Warnings returned when some requested load cases or modes did not have analysisresults in the response. (Filter Ids that don't exist in the model are rejectedup-front with HTTP 400 by the controller — they never reach this DTO.)`casesNotAnalyzed` is an SG list-format string that can be pasted straightinto `POST /job/analysis/run`'s `loadCases` field to re-run only thosecases. `modesNotAnalyzed` is a per-case list — each analysed case can computea different number of modes, so the warning is keyed by case rather than flattened.
    """
    # Load case Ids that exist in the model but produced no result rows for this query— typically because the analysis has not been run for those cases.SG list-format string (e.g. `"2,5-7"`) — already intersected against thecaller's original filter, ready to paste back into `POST /job/analysis/run`'s`loadCases` field.
    cases_not_analyzed: Optional[str] = None
    # Per-case list of modes the caller requested that did not produce result rowsfor that specific case. Each analysed case can compute a different number ofmodes, so a flattened across-cases warning would hide gaps. Each entry namesthe case and the SG list-format string of missing mode numbers for it.Informational — to resolve, raise the analysis `modes` count to at leastthe largest missing mode number and re-run.
    modes_not_analyzed: Optional[list[CaseModesWarning]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> QueryWarnings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: QueryWarnings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return QueryWarnings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .case_modes_warning import CaseModesWarning

        from .case_modes_warning import CaseModesWarning

        fields: dict[str, Callable[[Any], None]] = {
            "casesNotAnalyzed": lambda n : setattr(self, 'cases_not_analyzed', n.get_str_value()),
            "modesNotAnalyzed": lambda n : setattr(self, 'modes_not_analyzed', n.get_collection_of_object_values(CaseModesWarning)),
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
        writer.write_str_value("casesNotAnalyzed", self.cases_not_analyzed)
        writer.write_collection_of_object_values("modesNotAnalyzed", self.modes_not_analyzed)
    

