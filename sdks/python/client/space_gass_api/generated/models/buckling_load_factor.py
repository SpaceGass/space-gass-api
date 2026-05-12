from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class BucklingLoadFactor(Parsable):
    """
    Buckling load factor result (FileId 216).
    """
    # Load case ID.
    case: Optional[int] = None
    # Number of iterations to converge.
    iterations: Optional[int] = None
    # Buckling load factor.
    load_factor: Optional[float] = None
    # Buckling mode number.
    mode: Optional[int] = None
    # Node key at maximum rotation.
    node_at_max_rotn: Optional[float] = None
    # Node key at maximum translation.
    node_at_max_trans: Optional[float] = None
    # Axis of maximum rotation.
    rotn_axis: Optional[str] = None
    # Convergence tolerance.
    tolerance: Optional[float] = None
    # Axis of maximum translation.
    trans_axis: Optional[str] = None
    # Analysis engine warning message (empty if none).
    warning: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BucklingLoadFactor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BucklingLoadFactor
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BucklingLoadFactor()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "case": lambda n : setattr(self, 'case', n.get_int_value()),
            "iterations": lambda n : setattr(self, 'iterations', n.get_int_value()),
            "loadFactor": lambda n : setattr(self, 'load_factor', n.get_float_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_int_value()),
            "nodeAtMaxRotn": lambda n : setattr(self, 'node_at_max_rotn', n.get_float_value()),
            "nodeAtMaxTrans": lambda n : setattr(self, 'node_at_max_trans', n.get_float_value()),
            "rotnAxis": lambda n : setattr(self, 'rotn_axis', n.get_str_value()),
            "tolerance": lambda n : setattr(self, 'tolerance', n.get_float_value()),
            "transAxis": lambda n : setattr(self, 'trans_axis', n.get_str_value()),
            "warning": lambda n : setattr(self, 'warning', n.get_str_value()),
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
        writer.write_int_value("iterations", self.iterations)
        writer.write_float_value("loadFactor", self.load_factor)
        writer.write_int_value("mode", self.mode)
        writer.write_float_value("nodeAtMaxRotn", self.node_at_max_rotn)
        writer.write_float_value("nodeAtMaxTrans", self.node_at_max_trans)
        writer.write_str_value("rotnAxis", self.rotn_axis)
        writer.write_float_value("tolerance", self.tolerance)
        writer.write_str_value("transAxis", self.trans_axis)
        writer.write_str_value("warning", self.warning)
    

