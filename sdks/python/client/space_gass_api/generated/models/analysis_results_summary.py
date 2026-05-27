from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AnalysisResultsSummary(Parsable):
    """
    Summary of which analysis types have stored results for the current job.Values are read from Fortran result-file headers on disk — a lightweightheader-only read that does not load result datasheets.
    """
    # Whether buckling analysis results exist.
    has_buckling_results: Optional[bool] = None
    # Whether dynamic frequency analysis results exist.
    has_dynamic_results: Optional[bool] = None
    # Whether harmonic response analysis results exist.
    has_harmonic_results: Optional[bool] = None
    # Whether spectral response analysis results exist.
    has_spectral_results: Optional[bool] = None
    # Whether static analysis results exist (linear or non-linear).
    has_static_results: Optional[bool] = None
    # Whether transient dynamic analysis results exist.
    has_transient_results: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalysisResultsSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalysisResultsSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnalysisResultsSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "hasBucklingResults": lambda n : setattr(self, 'has_buckling_results', n.get_bool_value()),
            "hasDynamicResults": lambda n : setattr(self, 'has_dynamic_results', n.get_bool_value()),
            "hasHarmonicResults": lambda n : setattr(self, 'has_harmonic_results', n.get_bool_value()),
            "hasSpectralResults": lambda n : setattr(self, 'has_spectral_results', n.get_bool_value()),
            "hasStaticResults": lambda n : setattr(self, 'has_static_results', n.get_bool_value()),
            "hasTransientResults": lambda n : setattr(self, 'has_transient_results', n.get_bool_value()),
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
        writer.write_bool_value("hasBucklingResults", self.has_buckling_results)
        writer.write_bool_value("hasDynamicResults", self.has_dynamic_results)
        writer.write_bool_value("hasHarmonicResults", self.has_harmonic_results)
        writer.write_bool_value("hasSpectralResults", self.has_spectral_results)
        writer.write_bool_value("hasStaticResults", self.has_static_results)
        writer.write_bool_value("hasTransientResults", self.has_transient_results)
    

