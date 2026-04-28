from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Table(Parsable):
    """
    A generic 2D data table — row-major, where each row is an array of column values.Reused across the API for any tabular (X, Y, …) data such as restraintvariable-stiffness curves, derived force-vs-deflection views, material curves, etc.Schema (column names, types, units, bounds) is returned by the resource's dedicatedtable-metadata endpoint and is not embedded here.
    """
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Table:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Table
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Table()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
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
    

