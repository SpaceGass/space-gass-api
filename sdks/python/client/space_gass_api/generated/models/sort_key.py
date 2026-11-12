from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .result_sort_order import ResultSortOrder

@dataclass
class SortKey(Parsable):
    """
    The sort applied to a results page and, for each returned row, the value that ranked it.Arrays are parallel to `results`: entry `i` describes `results[i]`.
    """
    # The field the rows were sorted by, as named in the response.
    field: Optional[str] = None
    # Per row, the zero-based position of the governing element in the row's arrays(its station, member end, plate corner or node). Present only when the sort fieldis an array; `null` for a row with no value for the field.
    index: Optional[list[int]] = None
    # Direction for sorting result rows by a field: by value, or by magnitude ignoring sign.
    order: Optional[ResultSortOrder] = None
    # Per row, the signed value the row was ranked by, in the field's unit: the field'svalue for a flat row, or for an array field the governing element — the minimumfor `Asc`, the maximum for `Desc`, the largest magnitude for `AbsDesc`,the smallest magnitude for `AbsAsc`.`null` for a row with no value for the field (such rows sort last).
    value: Optional[list[float]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SortKey:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SortKey
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SortKey()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .result_sort_order import ResultSortOrder

        from .result_sort_order import ResultSortOrder

        fields: dict[str, Callable[[Any], None]] = {
            "field": lambda n : setattr(self, 'field', n.get_str_value()),
            "index": lambda n : setattr(self, 'index', n.get_collection_of_primitive_values(int)),
            "order": lambda n : setattr(self, 'order', n.get_enum_value(ResultSortOrder)),
            "value": lambda n : setattr(self, 'value', n.get_collection_of_primitive_values(float)),
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
        writer.write_str_value("field", self.field)
        writer.write_collection_of_primitive_values("index", self.index)
        writer.write_enum_value("order", self.order)
        writer.write_collection_of_primitive_values("value", self.value)
    

