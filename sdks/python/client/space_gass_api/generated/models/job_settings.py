from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .vertical_axis import VerticalAxis

@dataclass
class JobSettings(Parsable):
    """
    Read DTO for job-level settings.Groups configuration properties that apply to the job as a whole.
    """
    # Vertical (gravity) axis direction for the job.Determines which global axis is treated as the vertical/gravity direction.Maps to SPACE GASS CommonEnums.SGVerticalAxis (YAxis=2, ZAxis=3).Only YAxis and ZAxis are valid choices in SPACE GASS.
    vertical_axis: Optional[VerticalAxis] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .vertical_axis import VerticalAxis

        from .vertical_axis import VerticalAxis

        fields: dict[str, Callable[[Any], None]] = {
            "verticalAxis": lambda n : setattr(self, 'vertical_axis', n.get_enum_value(VerticalAxis)),
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
        writer.write_enum_value("verticalAxis", self.vertical_axis)
    

