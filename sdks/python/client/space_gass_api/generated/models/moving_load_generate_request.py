from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MovingLoadGenerateRequest(Parsable):
    """
    Optional request body for `POST moving-loads/generate`. The body itself is optional —omit it entirely to generate with the default load category.
    """
    # Id of an existing load category (GET /job/loads/load-categories) to tag the generatedload cases with. Omit, or send `null`, to reuse or create the default "Moving loads"category. `0` is not accepted: generated load cases always get a category. An unknownId is rejected with `400`.
    load_category: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MovingLoadGenerateRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MovingLoadGenerateRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MovingLoadGenerateRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "loadCategory": lambda n : setattr(self, 'load_category', n.get_int_value()),
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
        writer.write_int_value("loadCategory", self.load_category)
    

