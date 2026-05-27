from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .filter_mode import FilterMode
    from .filter_node_type import FilterNodeType

@dataclass
class FilterNodesUpdate(Parsable):
    """
    Partial update for the Nodes sub-filter.
    """
    # Whether this sub-filter participates in the filter.
    is_active: Optional[bool] = None
    # Whether a sub-filter block includes or excludes matching entities.
    mode: Optional[FilterMode] = None
    # Node type categories available as a Filter resource criterion.Mirrors SG's `SGItemFilter_NodeType` enum verbatim — integer valuesand labels match SG so the filter datasheet round-trips cleanly.Richer than the entity-property `NodeType` (which only has`All` / `Restrained`) because the filter UI surfaces everyfine-grained boundary-condition flavour.
    node_type: Optional[FilterNodeType] = None
    # The nodes property
    nodes: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilterNodesUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilterNodesUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FilterNodesUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .filter_mode import FilterMode
        from .filter_node_type import FilterNodeType

        from .filter_mode import FilterMode
        from .filter_node_type import FilterNodeType

        fields: dict[str, Callable[[Any], None]] = {
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_enum_value(FilterMode)),
            "nodeType": lambda n : setattr(self, 'node_type', n.get_enum_value(FilterNodeType)),
            "nodes": lambda n : setattr(self, 'nodes', n.get_str_value()),
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
        writer.write_bool_value("isActive", self.is_active)
        writer.write_enum_value("mode", self.mode)
        writer.write_enum_value("nodeType", self.node_type)
        writer.write_str_value("nodes", self.nodes)
    

