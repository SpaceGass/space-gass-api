from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MemberDistributedMomentKey(Parsable):
    """
    Composite Id object for bulk delete operations on member distributed moments.
    """
    # The load case number.
    load_case: Optional[int] = None
    # The member number.
    member: Optional[int] = None
    # The sub-load number.
    sub_load: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MemberDistributedMomentKey:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MemberDistributedMomentKey
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MemberDistributedMomentKey()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "member": lambda n : setattr(self, 'member', n.get_int_value()),
            "subLoad": lambda n : setattr(self, 'sub_load', n.get_int_value()),
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
        writer.write_int_value("loadCase", self.load_case)
        writer.write_int_value("member", self.member)
        writer.write_int_value("subLoad", self.sub_load)
    

