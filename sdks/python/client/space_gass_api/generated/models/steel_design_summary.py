from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SteelDesignSummary(Parsable):
    """
    Summary of which steel design types have stored results for the current job.Values are read from Fortran result-file headers on disk — a lightweightheader-only read that does not load result datasheets.
    """
    # Whether steel connection design results exist.
    has_connection_design_results: Optional[bool] = None
    # Whether steel member design results exist (check or design).
    has_member_design_results: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelDesignSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelDesignSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelDesignSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "hasConnectionDesignResults": lambda n : setattr(self, 'has_connection_design_results', n.get_bool_value()),
            "hasMemberDesignResults": lambda n : setattr(self, 'has_member_design_results', n.get_bool_value()),
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
        writer.write_bool_value("hasConnectionDesignResults", self.has_connection_design_results)
        writer.write_bool_value("hasMemberDesignResults", self.has_member_design_results)
    

