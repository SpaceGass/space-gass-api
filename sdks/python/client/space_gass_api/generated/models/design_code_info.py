from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .design_code import DesignCode

@dataclass
class DesignCodeInfo(Parsable):
    """
    A design code a design module can check or design to, the edition of the code arun is completed under, and whether this seat is licensed for it. Returned by themodule's codes endpoint (GET /job/design/steel-member/codes); no open job is needed.
    """
    # A design code (standard) a design module checks or designs to. The codes a modulesupports are listed by its codes endpoint, e.g. GET /job/design/steel-member/codes.
    code: Optional[DesignCode] = None
    # The edition of the code a run is completed under — the standard and its year.
    edition: Optional[str] = None
    # Whether this seat is licensed to run the code.
    is_licensed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DesignCodeInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DesignCodeInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DesignCodeInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .design_code import DesignCode

        from .design_code import DesignCode

        fields: dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_enum_value(DesignCode)),
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
    

