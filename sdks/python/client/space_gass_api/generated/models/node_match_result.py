from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .node_match import NodeMatch
    from .node_match_summary import NodeMatchSummary

@dataclass
class NodeMatchResult(Parsable):
    """
    The node at each requested position.
    """
    # One entry per requested position, in request order.
    matches: Optional[list[NodeMatch]] = None
    # Counts of the match outcomes. `existing + new + repeated` is the number of positions.
    summary: Optional[NodeMatchSummary] = None
    # The tolerance the positions were matched with: the one supplied, or the default.
    tolerance: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NodeMatchResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NodeMatchResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NodeMatchResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .node_match import NodeMatch
        from .node_match_summary import NodeMatchSummary

        from .node_match import NodeMatch
        from .node_match_summary import NodeMatchSummary

        fields: dict[str, Callable[[Any], None]] = {
            "matches": lambda n : setattr(self, 'matches', n.get_collection_of_object_values(NodeMatch)),
            "summary": lambda n : setattr(self, 'summary', n.get_object_value(NodeMatchSummary)),
            "tolerance": lambda n : setattr(self, 'tolerance', n.get_float_value()),
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
        writer.write_collection_of_object_values("matches", self.matches)
        writer.write_object_value("summary", self.summary)
        writer.write_float_value("tolerance", self.tolerance)
    

