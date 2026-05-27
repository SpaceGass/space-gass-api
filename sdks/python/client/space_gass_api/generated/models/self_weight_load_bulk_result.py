from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bulk_error import BulkError
    from .self_weight_load import SelfWeightLoad

@dataclass
class SelfWeightLoadBulkResult(Parsable):
    """
    Result of a bulk operation.
    """
    # Errors from failed items.
    errors: Optional[list[BulkError]] = None
    # True when the bulk operation stopped accumulating errors after reachingSpaceGassApi.Models.Dtos.Entity.BulkResultDto`1.ErrorMessageCap. Further failures may exist beyond what is reported.
    errors_truncated: Optional[bool] = None
    # Successfully processed items.
    succeeded: Optional[list[SelfWeightLoad]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SelfWeightLoadBulkResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SelfWeightLoadBulkResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SelfWeightLoadBulkResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .bulk_error import BulkError
        from .self_weight_load import SelfWeightLoad

        from .bulk_error import BulkError
        from .self_weight_load import SelfWeightLoad

        fields: dict[str, Callable[[Any], None]] = {
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(BulkError)),
            "errorsTruncated": lambda n : setattr(self, 'errors_truncated', n.get_bool_value()),
            "succeeded": lambda n : setattr(self, 'succeeded', n.get_collection_of_object_values(SelfWeightLoad)),
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
        writer.write_collection_of_object_values("errors", self.errors)
        writer.write_bool_value("errorsTruncated", self.errors_truncated)
        writer.write_collection_of_object_values("succeeded", self.succeeded)
    

