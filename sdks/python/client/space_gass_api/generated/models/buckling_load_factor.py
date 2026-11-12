from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mode_status import ModeStatus

@dataclass
class BucklingLoadFactor(Parsable):
    """
    Buckling load factor result (FileId 216).
    """
    # Number of iterations to converge. Null when `status` is not `Reported`.
    iterations: Optional[int] = None
    # Load case ID.
    load_case: Optional[int] = None
    # Buckling load factor. Null when `status` is not `Reported`.
    load_factor: Optional[float] = None
    # Buckling mode number.
    mode: Optional[int] = None
    # Id of the node with the maximum rotation in the mode shape. Null when `status` is not `Reported`.
    node_at_max_rotn: Optional[int] = None
    # Id of the node with the maximum translation in the mode shape. Null when `status` is not `Reported`.
    node_at_max_trans: Optional[int] = None
    # Axis of maximum rotation. Empty when `status` is not `Reported`.
    rotn_axis: Optional[str] = None
    # Whether the solver reported a value for a buckling or dynamic mode, and if not, why.
    status: Optional[ModeStatus] = None
    # Convergence tolerance. Null when `status` is not `Reported`.
    tolerance: Optional[float] = None
    # Axis of maximum translation. Empty when `status` is not `Reported`.
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
        from .mode_status import ModeStatus

        from .mode_status import ModeStatus

        fields: dict[str, Callable[[Any], None]] = {
            "iterations": lambda n : setattr(self, 'iterations', n.get_int_value()),
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "loadFactor": lambda n : setattr(self, 'load_factor', n.get_float_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_int_value()),
            "nodeAtMaxRotn": lambda n : setattr(self, 'node_at_max_rotn', n.get_int_value()),
            "nodeAtMaxTrans": lambda n : setattr(self, 'node_at_max_trans', n.get_int_value()),
            "rotnAxis": lambda n : setattr(self, 'rotn_axis', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ModeStatus)),
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
        writer.write_int_value("iterations", self.iterations)
        writer.write_int_value("loadCase", self.load_case)
        writer.write_float_value("loadFactor", self.load_factor)
        writer.write_int_value("mode", self.mode)
        writer.write_int_value("nodeAtMaxRotn", self.node_at_max_rotn)
        writer.write_int_value("nodeAtMaxTrans", self.node_at_max_trans)
        writer.write_str_value("rotnAxis", self.rotn_axis)
        writer.write_enum_value("status", self.status)
        writer.write_float_value("tolerance", self.tolerance)
        writer.write_str_value("transAxis", self.trans_axis)
        writer.write_str_value("warning", self.warning)
    

