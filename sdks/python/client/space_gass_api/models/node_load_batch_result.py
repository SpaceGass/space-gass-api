from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .batch_error import BatchError
    from .node_load import NodeLoad

@dataclass
class NodeLoadBatchResult(Parsable):
    """
    Result of a batch operation.
    """
    # Errors from failed items.
    errors: Optional[list[BatchError]] = None
    # True when the bulk operation stopped accumulating errors after reachingSpaceGassApi.Models.Dtos.Entity.BatchResultDto`1.ErrorMessageCap. Further failures may exist beyond what is reported.
    errors_truncated: Optional[bool] = None
    # Successfully processed items.
    succeeded: Optional[list[NodeLoad]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NodeLoadBatchResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NodeLoadBatchResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NodeLoadBatchResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .batch_error import BatchError
        from .node_load import NodeLoad

        from .batch_error import BatchError
        from .node_load import NodeLoad

        fields: dict[str, Callable[[Any], None]] = {
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(BatchError)),
            "errorsTruncated": lambda n : setattr(self, 'errors_truncated', n.get_bool_value()),
            "succeeded": lambda n : setattr(self, 'succeeded', n.get_collection_of_object_values(NodeLoad)),
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
    

