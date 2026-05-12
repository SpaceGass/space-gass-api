from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .field_metadata import FieldMetadata

@dataclass
class TableMetadata(Parsable):
    """
    Schema metadata for a generic 2D data table — display title, per-column metadata(reusing SpaceGassApi.Models.Dtos.Common.FieldMetadataDto for parity with the rest of the API'smetadata responses), and the maximum number of rows the table accepts.
    """
    # Column metadata in the same order the values appear in each row of SpaceGassApi.Models.Dtos.Common.TableDto.Rows.Each entry uses the same SpaceGassApi.Models.Dtos.Common.FieldMetadataDto shape as resource-levelmetadata (`jsonName`, `dataType`, `units`, `min`, `max`,`description`).
    columns: Optional[list[FieldMetadata]] = None
    # Maximum number of rows the table accepts.
    max_rows: Optional[int] = None
    # Human-readable title, e.g. "Stiffness vs Deflection".
    table_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TableMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TableMetadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TableMetadata()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .field_metadata import FieldMetadata

        from .field_metadata import FieldMetadata

        fields: dict[str, Callable[[Any], None]] = {
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(FieldMetadata)),
            "maxRows": lambda n : setattr(self, 'max_rows', n.get_int_value()),
            "tableName": lambda n : setattr(self, 'table_name', n.get_str_value()),
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
        writer.write_collection_of_object_values("columns", self.columns)
        writer.write_int_value("maxRows", self.max_rows)
        writer.write_str_value("tableName", self.table_name)
    

