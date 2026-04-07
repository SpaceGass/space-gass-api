from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .member_intermediate_force import MemberIntermediateForce
    from .query_warnings import QueryWarnings

@dataclass
class MemberIntermediateForceQueryResult(Parsable):
    """
    Wrapper for analysis query results.Contains the result data plus optional warnings about requested keys or cases that were skipped.
    """
    # The query result rows.
    results: Optional[list[MemberIntermediateForce]] = None
    # Warnings returned when query filter parameters reference keys or load casesthat do not exist in the result set.
    warnings: Optional[QueryWarnings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MemberIntermediateForceQueryResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MemberIntermediateForceQueryResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MemberIntermediateForceQueryResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .member_intermediate_force import MemberIntermediateForce
        from .query_warnings import QueryWarnings

        from .member_intermediate_force import MemberIntermediateForce
        from .query_warnings import QueryWarnings

        fields: dict[str, Callable[[Any], None]] = {
            "results": lambda n : setattr(self, 'results', n.get_collection_of_object_values(MemberIntermediateForce)),
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
    

