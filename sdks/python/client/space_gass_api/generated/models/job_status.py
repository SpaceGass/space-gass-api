from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_mode import AccessMode
    from .analysis_results_summary import AnalysisResultsSummary
    from .job import Job
    from .job_state import JobState
    from .loads_summary import LoadsSummary
    from .steel_design_summary import SteelDesignSummary
    from .structure_summary import StructureSummary

@dataclass
class JobStatus(Parsable):
    """
    Full job status response including the current job, session state, structure summary, and loads summary.Returned by lifecycle operations (new, open, save, status) and GET /job/status.
    """
    # Current operational mode of the API.
    access_mode: Optional[AccessMode] = None
    # Summary of which analysis types have stored results for the current job.Values are read from Fortran result-file headers on disk — a lightweightheader-only read that does not load result datasheets.
    analysis: Optional[AnalysisResultsSummary] = None
    # Read DTO for job responses.Model counts and file state are available via GET /job/status (JobStatusDto).
    job: Optional[Job] = None
    # Summary counts of load-related entities in the current job — load casemanagement and all applied load types.
    loads: Optional[LoadsSummary] = None
    # Current session/file state of the job.
    state: Optional[JobState] = None
    # Summary of steel design data and results for the current job — the number ofsteel member design groups, and which steel design types have stored results.Result flags are read from Fortran result-file headers on disk — a lightweightheader-only read that does not load result datasheets.
    steel_design: Optional[SteelDesignSummary] = None
    # Summary counts of structural entities in the current job — geometry,boundary conditions, and section/material properties.
    structure: Optional[StructureSummary] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_mode import AccessMode
        from .analysis_results_summary import AnalysisResultsSummary
        from .job import Job
        from .job_state import JobState
        from .loads_summary import LoadsSummary
        from .steel_design_summary import SteelDesignSummary
        from .structure_summary import StructureSummary

        from .access_mode import AccessMode
        from .analysis_results_summary import AnalysisResultsSummary
        from .job import Job
        from .job_state import JobState
        from .loads_summary import LoadsSummary
        from .steel_design_summary import SteelDesignSummary
        from .structure_summary import StructureSummary

        fields: dict[str, Callable[[Any], None]] = {
            "accessMode": lambda n : setattr(self, 'access_mode', n.get_enum_value(AccessMode)),
            "analysis": lambda n : setattr(self, 'analysis', n.get_object_value(AnalysisResultsSummary)),
            "job": lambda n : setattr(self, 'job', n.get_object_value(Job)),
            "loads": lambda n : setattr(self, 'loads', n.get_object_value(LoadsSummary)),
            "state": lambda n : setattr(self, 'state', n.get_object_value(JobState)),
            "steelDesign": lambda n : setattr(self, 'steel_design', n.get_object_value(SteelDesignSummary)),
            "structure": lambda n : setattr(self, 'structure', n.get_object_value(StructureSummary)),
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
        writer.write_enum_value("accessMode", self.access_mode)
        writer.write_object_value("analysis", self.analysis)
        writer.write_object_value("job", self.job)
        writer.write_object_value("loads", self.loads)
        writer.write_object_value("state", self.state)
        writer.write_object_value("steelDesign", self.steel_design)
        writer.write_object_value("structure", self.structure)
    

