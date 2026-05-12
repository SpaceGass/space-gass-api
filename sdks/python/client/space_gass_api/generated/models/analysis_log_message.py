from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analysis_log_level import AnalysisLogLevel

@dataclass
class AnalysisLogMessage(Parsable):
    """
    A log message from the analysis solver
    """
    # Log level for analysis messages
    level: Optional[AnalysisLogLevel] = None
    # The message text
    text: Optional[str] = None
    # When the message was received
    timestamp: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalysisLogMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalysisLogMessage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnalysisLogMessage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .analysis_log_level import AnalysisLogLevel

        from .analysis_log_level import AnalysisLogLevel

        fields: dict[str, Callable[[Any], None]] = {
            "level": lambda n : setattr(self, 'level', n.get_enum_value(AnalysisLogLevel)),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_datetime_value()),
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
        writer.write_enum_value("level", self.level)
        writer.write_str_value("text", self.text)
        writer.write_datetime_value("timestamp", self.timestamp)
    

