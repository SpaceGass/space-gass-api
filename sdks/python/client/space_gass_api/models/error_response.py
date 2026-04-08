from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.api_error import APIError
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .error_response_extensions import ErrorResponse_extensions
    from .error_source import ErrorSource
    from .validation_error import ValidationError

@dataclass
class ErrorResponse(APIError, Parsable):
    """
    Standard error response format for all API errorsFollows RFC 7807 Problem Details pattern
    """
    # A human-readable explanation specific to this occurrence
    detail: Optional[str] = None
    # Machine-readable error code for programmatic handling
    error_code: Optional[str] = None
    # List of validation errors (if applicable)
    errors: Optional[list[ValidationError]] = None
    # Additional context-specific data
    extensions: Optional[ErrorResponse_extensions] = None
    # A URI reference that identifies the specific occurrence
    instance: Optional[str] = None
    # Source of the error
    source: Optional[ErrorSource] = None
    # HTTP status code
    status: Optional[int] = None
    # Timestamp when the error occurred
    timestamp: Optional[datetime.datetime] = None
    # A short, human-readable summary of the problem type
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ErrorResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ErrorResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ErrorResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .error_response_extensions import ErrorResponse_extensions
        from .error_source import ErrorSource
        from .validation_error import ValidationError

        from .error_response_extensions import ErrorResponse_extensions
        from .error_source import ErrorSource
        from .validation_error import ValidationError

        fields: dict[str, Callable[[Any], None]] = {
            "detail": lambda n : setattr(self, 'detail', n.get_str_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(ValidationError)),
            "extensions": lambda n : setattr(self, 'extensions', n.get_object_value(ErrorResponse_extensions)),
            "instance": lambda n : setattr(self, 'instance', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(ErrorSource)),
            "status": lambda n : setattr(self, 'status', n.get_int_value()),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_datetime_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("detail", self.detail)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_collection_of_object_values("errors", self.errors)
        writer.write_object_value("extensions", self.extensions)
        writer.write_str_value("instance", self.instance)
        writer.write_enum_value("source", self.source)
        writer.write_int_value("status", self.status)
        writer.write_datetime_value("timestamp", self.timestamp)
        writer.write_str_value("title", self.title)
    
    @property
    def primary_message(self) -> Optional[str]:
        """
        The primary error message.
        """
        return super().message

