from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .load_factor_type import LoadFactorType
    from .query_warnings import QueryWarnings
    from .sort_key import SortKey
    from .steel_check_summary import SteelCheckSummary

@dataclass
class SteelCheckSummaryQueryResult(Parsable):
    """
    The steel member check summary: the rows (one per steel member the stored resultscover, SpaceGassApi.Models.Dtos.Query.Design.SteelCheckSummaryDto) plus what the stored results say as a whole —the design code they were produced under, what their load factors are, and the steelmembers they do not cover.
    """
    # SPACE GASS's own label for the design code and edition the stored results wereproduced under — the same string as job/status's `steelDesign.steelMemberDesignCode`(e.g. `AS4100:2020`, `AISC 360-22 (LRFD)`, `AS1250 1981`). A displaystring, not a fixed set of values; `loadFactorType` is the value to switch on.Every row was produced under it: SPACE GASS removes all stored results when thedesign code changes. `null` when SPACE GASS has no label for the stored code.
    design_code: Optional[str] = None
    # What a steel member design result's `loadFactor` (and its `loadFactorLimit`)is, which depends on the design code the results were produced under.
    load_factor_type: Optional[LoadFactorType] = None
    # Steel members (design groups) the stored results do not cover — those with no row —in SG list format, empty when every steel member has a row. With a `steelMembers`filter only the filtered Ids are considered. Computed before value filters and paging,so it is the same on every page.
    not_designed: Optional[str] = None
    # The query result rows.
    results: Optional[list[SteelCheckSummary]] = None
    # The sort applied to a results page and, for each returned row, the value that ranked it.Arrays are parallel to `results`: entry `i` describes `results[i]`.
    sort_key: Optional[SortKey] = None
    # Warnings returned when some requested load cases or modes did not have analysisresults in the response. (Filter Ids that don't exist in the model are rejectedup-front with HTTP 400 by the controller — they never reach this DTO.)`loadCasesNotAnalyzed` is an SG list-format string that can be pasted straightinto `POST /job/analysis/run`'s `loadCases` field to re-run only thosecases. `modesNotAnalyzed` is a per-case list — each analysed case can computea different number of modes, so the warning is keyed by case rather than flattened.
    warnings: Optional[QueryWarnings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelCheckSummaryQueryResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelCheckSummaryQueryResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelCheckSummaryQueryResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .load_factor_type import LoadFactorType
        from .query_warnings import QueryWarnings
        from .sort_key import SortKey
        from .steel_check_summary import SteelCheckSummary

        from .load_factor_type import LoadFactorType
        from .query_warnings import QueryWarnings
        from .sort_key import SortKey
        from .steel_check_summary import SteelCheckSummary

        fields: dict[str, Callable[[Any], None]] = {
            "designCode": lambda n : setattr(self, 'design_code', n.get_str_value()),
            "loadFactorType": lambda n : setattr(self, 'load_factor_type', n.get_enum_value(LoadFactorType)),
            "notDesigned": lambda n : setattr(self, 'not_designed', n.get_str_value()),
            "results": lambda n : setattr(self, 'results', n.get_collection_of_object_values(SteelCheckSummary)),
            "sortKey": lambda n : setattr(self, 'sort_key', n.get_object_value(SortKey)),
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
        writer.write_str_value("designCode", self.design_code)
        writer.write_enum_value("loadFactorType", self.load_factor_type)
        writer.write_str_value("notDesigned", self.not_designed)
        writer.write_collection_of_object_values("results", self.results)
        writer.write_object_value("sortKey", self.sort_key)
        writer.write_object_value("warnings", self.warnings)
    

