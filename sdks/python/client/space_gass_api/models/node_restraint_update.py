from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .friction_normal_axis import FrictionNormalAxis
    from .friction_normal_direction import FrictionNormalDirection

@dataclass
class NodeRestraintUpdate(Parsable):
    """
    DTO for partial updates to a node restraint.All fields are nullable — only provided fields are updated.
    """
    # 6-character active direction code for TX,TY,TZ,RX,RY,RZ.Each character: B=Both, P=Positive only, N=Negative only.
    active_direction: Optional[str] = None
    # Whether this is a general restraint.
    general_restraint: Optional[bool] = None
    # The node number that identifies which restraint to update.Required for bulk PATCH (PATCH /restraints/bulk).Ignored for single-node PATCH (PATCH /{key}/restraint) — the route value is used instead.
    node: Optional[int] = None
    # 6-character restraint code for TX,TY,TZ,RX,RY,RZ.Each character: F=Free, R=Restrained, S=Spring, V=Variable spring, P=Plastic, N=Nonlinear friction.
    restraint_code: Optional[str] = None
    # Rotational X plastic limit. Unit: Moment (see GET /job/units).
    rx_plastic_limit: Optional[float] = None
    # Rotational X spring stiffness. Unit: Moment/Radian (see GET /job/units).
    rx_stiffness: Optional[float] = None
    # Rotational Y plastic limit. Unit: Moment (see GET /job/units).
    ry_plastic_limit: Optional[float] = None
    # Rotational Y spring stiffness. Unit: Moment/Radian (see GET /job/units).
    ry_stiffness: Optional[float] = None
    # Rotational Z plastic limit. Unit: Moment (see GET /job/units).
    rz_plastic_limit: Optional[float] = None
    # Rotational Z spring stiffness. Unit: Moment/Radian (see GET /job/units).
    rz_stiffness: Optional[float] = None
    # Translational X plastic limit. Unit: Force (see GET /job/units).
    tx_plastic_limit: Optional[float] = None
    # Translational X spring stiffness. Unit: Force/Length (see GET /job/units).
    tx_stiffness: Optional[float] = None
    # Translational Y plastic limit. Unit: Force (see GET /job/units).
    ty_plastic_limit: Optional[float] = None
    # Translational Y spring stiffness. Unit: Force/Length (see GET /job/units).
    ty_stiffness: Optional[float] = None
    # Translational Z plastic limit. Unit: Force (see GET /job/units).
    tz_plastic_limit: Optional[float] = None
    # Translational Z spring stiffness. Unit: Force/Length (see GET /job/units).
    tz_stiffness: Optional[float] = None
    # X-axis friction factor.
    x_friction_factor: Optional[float] = None
    # Friction normal axis for restraint friction definitions.Maps to SPACE GASS lookup table "N/X/Y/Z Axes".
    x_friction_normal_axis: Optional[FrictionNormalAxis] = None
    # Friction normal direction for restraint friction definitions.Maps to SPACE GASS lookup table "Normal Direction".
    x_friction_normal_direction: Optional[FrictionNormalDirection] = None
    # Y-axis friction factor.
    y_friction_factor: Optional[float] = None
    # Friction normal axis for restraint friction definitions.Maps to SPACE GASS lookup table "N/X/Y/Z Axes".
    y_friction_normal_axis: Optional[FrictionNormalAxis] = None
    # Friction normal direction for restraint friction definitions.Maps to SPACE GASS lookup table "Normal Direction".
    y_friction_normal_direction: Optional[FrictionNormalDirection] = None
    # Z-axis friction factor.
    z_friction_factor: Optional[float] = None
    # Friction normal axis for restraint friction definitions.Maps to SPACE GASS lookup table "N/X/Y/Z Axes".
    z_friction_normal_axis: Optional[FrictionNormalAxis] = None
    # Friction normal direction for restraint friction definitions.Maps to SPACE GASS lookup table "Normal Direction".
    z_friction_normal_direction: Optional[FrictionNormalDirection] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NodeRestraintUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NodeRestraintUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NodeRestraintUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .friction_normal_axis import FrictionNormalAxis
        from .friction_normal_direction import FrictionNormalDirection

        from .friction_normal_axis import FrictionNormalAxis
        from .friction_normal_direction import FrictionNormalDirection

        fields: dict[str, Callable[[Any], None]] = {
            "activeDirection": lambda n : setattr(self, 'active_direction', n.get_str_value()),
            "generalRestraint": lambda n : setattr(self, 'general_restraint', n.get_bool_value()),
            "node": lambda n : setattr(self, 'node', n.get_int_value()),
            "restraintCode": lambda n : setattr(self, 'restraint_code', n.get_str_value()),
            "rxPlasticLimit": lambda n : setattr(self, 'rx_plastic_limit', n.get_float_value()),
            "rxStiffness": lambda n : setattr(self, 'rx_stiffness', n.get_float_value()),
            "ryPlasticLimit": lambda n : setattr(self, 'ry_plastic_limit', n.get_float_value()),
            "ryStiffness": lambda n : setattr(self, 'ry_stiffness', n.get_float_value()),
            "rzPlasticLimit": lambda n : setattr(self, 'rz_plastic_limit', n.get_float_value()),
            "rzStiffness": lambda n : setattr(self, 'rz_stiffness', n.get_float_value()),
            "txPlasticLimit": lambda n : setattr(self, 'tx_plastic_limit', n.get_float_value()),
            "txStiffness": lambda n : setattr(self, 'tx_stiffness', n.get_float_value()),
            "tyPlasticLimit": lambda n : setattr(self, 'ty_plastic_limit', n.get_float_value()),
            "tyStiffness": lambda n : setattr(self, 'ty_stiffness', n.get_float_value()),
            "tzPlasticLimit": lambda n : setattr(self, 'tz_plastic_limit', n.get_float_value()),
            "tzStiffness": lambda n : setattr(self, 'tz_stiffness', n.get_float_value()),
            "xFrictionFactor": lambda n : setattr(self, 'x_friction_factor', n.get_float_value()),
            "xFrictionNormalAxis": lambda n : setattr(self, 'x_friction_normal_axis', n.get_enum_value(FrictionNormalAxis)),
            "xFrictionNormalDirection": lambda n : setattr(self, 'x_friction_normal_direction', n.get_enum_value(FrictionNormalDirection)),
            "yFrictionFactor": lambda n : setattr(self, 'y_friction_factor', n.get_float_value()),
            "yFrictionNormalAxis": lambda n : setattr(self, 'y_friction_normal_axis', n.get_enum_value(FrictionNormalAxis)),
            "yFrictionNormalDirection": lambda n : setattr(self, 'y_friction_normal_direction', n.get_enum_value(FrictionNormalDirection)),
            "zFrictionFactor": lambda n : setattr(self, 'z_friction_factor', n.get_float_value()),
            "zFrictionNormalAxis": lambda n : setattr(self, 'z_friction_normal_axis', n.get_enum_value(FrictionNormalAxis)),
            "zFrictionNormalDirection": lambda n : setattr(self, 'z_friction_normal_direction', n.get_enum_value(FrictionNormalDirection)),
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
        writer.write_str_value("activeDirection", self.active_direction)
        writer.write_bool_value("generalRestraint", self.general_restraint)
        writer.write_int_value("node", self.node)
        writer.write_str_value("restraintCode", self.restraint_code)
        writer.write_float_value("rxPlasticLimit", self.rx_plastic_limit)
        writer.write_float_value("rxStiffness", self.rx_stiffness)
        writer.write_float_value("ryPlasticLimit", self.ry_plastic_limit)
        writer.write_float_value("ryStiffness", self.ry_stiffness)
        writer.write_float_value("rzPlasticLimit", self.rz_plastic_limit)
        writer.write_float_value("rzStiffness", self.rz_stiffness)
        writer.write_float_value("txPlasticLimit", self.tx_plastic_limit)
        writer.write_float_value("txStiffness", self.tx_stiffness)
        writer.write_float_value("tyPlasticLimit", self.ty_plastic_limit)
        writer.write_float_value("tyStiffness", self.ty_stiffness)
        writer.write_float_value("tzPlasticLimit", self.tz_plastic_limit)
        writer.write_float_value("tzStiffness", self.tz_stiffness)
        writer.write_float_value("xFrictionFactor", self.x_friction_factor)
        writer.write_enum_value("xFrictionNormalAxis", self.x_friction_normal_axis)
        writer.write_enum_value("xFrictionNormalDirection", self.x_friction_normal_direction)
        writer.write_float_value("yFrictionFactor", self.y_friction_factor)
        writer.write_enum_value("yFrictionNormalAxis", self.y_friction_normal_axis)
        writer.write_enum_value("yFrictionNormalDirection", self.y_friction_normal_direction)
        writer.write_float_value("zFrictionFactor", self.z_friction_factor)
        writer.write_enum_value("zFrictionNormalAxis", self.z_friction_normal_axis)
        writer.write_enum_value("zFrictionNormalDirection", self.z_friction_normal_direction)
    

