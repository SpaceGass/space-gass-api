from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LoadCaseModesWarning(Parsable):
    """
    One case's missing-mode entry inside SpaceGassApi.Models.Dtos.Query.Analysis.QueryWarningsDto.ModesNotAnalyzed.
    """
    # Load case Id this entry applies to.
    load_case: Optional[int] = None
    # Mode numbers the caller requested but the analysis did not produce for this case.SG list-format string.
    modes: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LoadCaseModesWarning:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LoadCaseModesWarning
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LoadCaseModesWarning()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "modes": lambda n : setattr(self, 'modes', n.get_str_value()),
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
        writer.write_int_value("loadCase", self.load_case)
        writer.write_str_value("modes", self.modes)
    

