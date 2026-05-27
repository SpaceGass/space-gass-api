from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .solver_type import SolverType

@dataclass
class AnalysisLoadCaseInfo(Parsable):
    """
    Per-case summary inside SpaceGassApi.Models.Dtos.Analysis.AnalysisInfoDto.LoadCases.Every requested case appears in the array; SpaceGassApi.Models.Dtos.Analysis.AnalysisLoadCaseInfoDto.HasResults indicateswhether result data fields (SpaceGassApi.Models.Dtos.Analysis.AnalysisLoadCaseInfoDto.Solver, SpaceGassApi.Models.Dtos.Analysis.AnalysisLoadCaseInfoDto.IsNonLinear,SpaceGassApi.Models.Dtos.Analysis.AnalysisLoadCaseInfoDto.Modes) are populated.
    """
    # Whether this case has stored results for the analysis type.When `false`, the remaining fields are omitted.
    has_results: Optional[bool] = None
    # Whether this case was analysed non-linearly. Populated for staticanalysis cases that have results; omitted otherwise.
    is_non_linear: Optional[bool] = None
    # The load case Id.
    load_case: Optional[int] = None
    # Number of buckling or dynamic modes computed for this case.Populated for buckling/dynamic analysis cases that have results;omitted otherwise.
    modes: Optional[int] = None
    # Matrix solver type used by the analysis engine.Integer values mirror SPACE GASS's `SGSolverType` enum(NetCommon/CommonEnums.vb): 0=Paradise, 1=Wavefront, 2=Watcom (legacy,not exposed), 3=SG-X (cloud, dispatched externally — not yet supportedby the in-process API analysis path).
    solver: Optional[SolverType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalysisLoadCaseInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalysisLoadCaseInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnalysisLoadCaseInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .solver_type import SolverType

        from .solver_type import SolverType

        fields: dict[str, Callable[[Any], None]] = {
            "hasResults": lambda n : setattr(self, 'has_results', n.get_bool_value()),
            "isNonLinear": lambda n : setattr(self, 'is_non_linear', n.get_bool_value()),
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "modes": lambda n : setattr(self, 'modes', n.get_int_value()),
            "solver": lambda n : setattr(self, 'solver', n.get_enum_value(SolverType)),
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
        writer.write_bool_value("isNonLinear", self.is_non_linear)
        writer.write_int_value("loadCase", self.load_case)
        writer.write_int_value("modes", self.modes)
        writer.write_enum_value("solver", self.solver)
    

