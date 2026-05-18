from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MemberPrestressLoadUpdate(Parsable):
    """
    DTO for updating an existing member prestress load.Only fields included in the request are updated; omit a field to keep its current value.
    """
    # The load case number.
    case: Optional[int] = None
    # Load category for grouping/organization.
    load_category: Optional[int] = None
    # The member number.
    member: Optional[int] = None
    # Prestress force applied to the member.
    prestress: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MemberPrestressLoadUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MemberPrestressLoadUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MemberPrestressLoadUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "case": lambda n : setattr(self, 'case', n.get_int_value()),
            "loadCategory": lambda n : setattr(self, 'load_category', n.get_int_value()),
            "member": lambda n : setattr(self, 'member', n.get_int_value()),
            "prestress": lambda n : setattr(self, 'prestress', n.get_float_value()),
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
        writer.write_int_value("case", self.case)
        writer.write_int_value("loadCategory", self.load_category)
        writer.write_int_value("member", self.member)
        writer.write_float_value("prestress", self.prestress)
    

