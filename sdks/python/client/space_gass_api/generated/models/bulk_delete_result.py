from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bulk_deleted import BulkDeleted
    from .bulk_error import BulkError
    from .delete_result import DeleteResult

@dataclass
class BulkDeleteResult(Parsable):
    """
    Bulk delete result for nodes, members and plates, plus the batch's cascade.
    """
    # Errors from failed items.
    errors: Optional[list[BulkError]] = None
    # True when the bulk operation stopped accumulating errors after reachingSpaceGassApi.Models.Dtos.Entity.BulkResultDto`1.ErrorMessageCap. Further failures may exist beyond what is reported.
    errors_truncated: Optional[bool] = None
    # Summary of a cascade delete: everything removed when a Node, Member, or Plate was deleted —the entity itself plus every child row that referenced it and any nodes transitively orphanedby the removal. Only entity types that actually had rows removed are present; the rest are omitted.Notes and dimensions attached to removed items are removed from the job settings but not listed.
    removed: Optional[DeleteResult] = None
    # Successfully processed items.
    succeeded: Optional[list[BulkDeleted]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BulkDeleteResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BulkDeleteResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BulkDeleteResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .bulk_deleted import BulkDeleted
        from .bulk_error import BulkError
        from .delete_result import DeleteResult

        from .bulk_deleted import BulkDeleted
        from .bulk_error import BulkError
        from .delete_result import DeleteResult

        fields: dict[str, Callable[[Any], None]] = {
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(BulkError)),
            "errorsTruncated": lambda n : setattr(self, 'errors_truncated', n.get_bool_value()),
            "removed": lambda n : setattr(self, 'removed', n.get_object_value(DeleteResult)),
            "succeeded": lambda n : setattr(self, 'succeeded', n.get_collection_of_object_values(BulkDeleted)),
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
        writer.write_object_value("removed", self.removed)
        writer.write_collection_of_object_values("succeeded", self.succeeded)
    

