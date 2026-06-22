from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LumpedMassLoadCreate(Parsable):
    """
    DTO for creating a new lumped mass load.
    """
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # The load case number to create this load in.
    load_case: Optional[int] = None
    # Load category for grouping/organization.
    load_category: Optional[int] = None
    # The node number to apply this lumped mass to.
    node: Optional[int] = None
    # Rotational mass inertia about the global X axis.
    rmx: Optional[float] = None
    # Rotational mass inertia about the global Y axis.
    rmy: Optional[float] = None
    # Rotational mass inertia about the global Z axis.
    rmz: Optional[float] = None
    # Translational mass in the global X direction.
    tmx: Optional[float] = None
    # Translational mass in the global Y direction.
    tmy: Optional[float] = None
    # Translational mass in the global Z direction.
    tmz: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LumpedMassLoadCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LumpedMassLoadCreate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LumpedMassLoadCreate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "loadCategory": lambda n : setattr(self, 'load_category', n.get_int_value()),
            "node": lambda n : setattr(self, 'node', n.get_int_value()),
            "rmx": lambda n : setattr(self, 'rmx', n.get_float_value()),
            "rmy": lambda n : setattr(self, 'rmy', n.get_float_value()),
            "rmz": lambda n : setattr(self, 'rmz', n.get_float_value()),
            "tmx": lambda n : setattr(self, 'tmx', n.get_float_value()),
            "tmy": lambda n : setattr(self, 'tmy', n.get_float_value()),
            "tmz": lambda n : setattr(self, 'tmz', n.get_float_value()),
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
        writer.write_str_value("guid", self.guid)
        writer.write_int_value("loadCase", self.load_case)
        writer.write_int_value("loadCategory", self.load_category)
        writer.write_int_value("node", self.node)
        writer.write_float_value("rmx", self.rmx)
        writer.write_float_value("rmy", self.rmy)
        writer.write_float_value("rmz", self.rmz)
        writer.write_float_value("tmx", self.tmx)
        writer.write_float_value("tmy", self.tmy)
        writer.write_float_value("tmz", self.tmz)
    

