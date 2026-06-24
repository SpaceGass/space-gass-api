from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MovingLoadGenerationResult(Parsable):
    """
    Result of a moving-load case-generation run. The generated load cases themselves are readthrough the standard load-case endpoints; this carries the discovered identifiers and thenames of the selection groups that were (re)built.
    """
    # The names of the load-case selection groups created for the generated cases.
    generated_groups: Optional[list[str]] = None
    # The Ids of all moving-load load cases present after generation.
    generated_load_case_ids: Optional[list[int]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MovingLoadGenerationResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MovingLoadGenerationResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MovingLoadGenerationResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "generatedGroups": lambda n : setattr(self, 'generated_groups', n.get_collection_of_primitive_values(str)),
            "generatedLoadCaseIds": lambda n : setattr(self, 'generated_load_case_ids', n.get_collection_of_primitive_values(int)),
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
        writer.write_collection_of_primitive_values("generatedGroups", self.generated_groups)
        writer.write_collection_of_primitive_values("generatedLoadCaseIds", self.generated_load_case_ids)
    

