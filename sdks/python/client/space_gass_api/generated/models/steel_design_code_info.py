from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .steel_design_code import SteelDesignCode

@dataclass
class SteelDesignCodeInfo(Parsable):
    """
    A steel member design code the API can check or design to, the edition of thecode a run is completed under, and whether this seat is licensed for it.Returned by GET /job/design/steel-design/codes; no open job is needed.
    """
    # Steel member design code used to check or design steel members.
    code: Optional[SteelDesignCode] = None
    # The edition of the code a run is completed under — the standard and its year.
    edition: Optional[str] = None
    # Whether this seat is licensed to run the code.
    is_licensed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelDesignCodeInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelDesignCodeInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelDesignCodeInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .steel_design_code import SteelDesignCode

        from .steel_design_code import SteelDesignCode

        fields: dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_enum_value(SteelDesignCode)),
            "edition": lambda n : setattr(self, 'edition', n.get_str_value()),
            "isLicensed": lambda n : setattr(self, 'is_licensed', n.get_bool_value()),
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
        writer.write_enum_value("code", self.code)
        writer.write_str_value("edition", self.edition)
        writer.write_bool_value("isLicensed", self.is_licensed)
    

