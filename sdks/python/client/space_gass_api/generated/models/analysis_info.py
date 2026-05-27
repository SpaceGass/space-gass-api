from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analysis_load_case_info import AnalysisLoadCaseInfo

@dataclass
class AnalysisInfo(Parsable):
    """
    Lightweight pre-flight summary of which load cases have results for a givenanalysis type, used by clients to decide whether a results query is worth issuing(and which cases still need to be analysed).
    """
    # True when any analysis of this type has been run and at least one casehas stored results. Determined from the file header — does not requireloading the full result datasheet.
    has_results: Optional[bool] = None
    # Per-case result status, optionally restricted to the caller-supplied`loadCases` filter. Every requested case appears in the array; eachentry's SpaceGassApi.Models.Dtos.Analysis.AnalysisLoadCaseInfoDto.HasResults indicates whetherresult data is available.
    load_cases: Optional[list[AnalysisLoadCaseInfo]] = None
    # SG list-format string of load case Ids that exist in the model but havenot been analysed for this analysis type. When the caller supplied a`cases` filter, this is the intersection of that filter with thenot-analysed set — ready to paste straight back into the relevant`POST /job/analysis/.../run` body.Omitted when every relevant case has been analysed.
    not_analyzed: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalysisInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalysisInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnalysisInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .analysis_load_case_info import AnalysisLoadCaseInfo

        from .analysis_load_case_info import AnalysisLoadCaseInfo

        fields: dict[str, Callable[[Any], None]] = {
            "hasResults": lambda n : setattr(self, 'has_results', n.get_bool_value()),
            "loadCases": lambda n : setattr(self, 'load_cases', n.get_collection_of_object_values(AnalysisLoadCaseInfo)),
            "notAnalyzed": lambda n : setattr(self, 'not_analyzed', n.get_str_value()),
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
        writer.write_bool_value("hasResults", self.has_results)
        writer.write_collection_of_object_values("loadCases", self.load_cases)
        writer.write_str_value("notAnalyzed", self.not_analyzed)
    

