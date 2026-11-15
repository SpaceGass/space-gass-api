from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ifc_convert_to import IfcConvertTo
    from .ifc_schema import IfcSchema

@dataclass
class IfcExportSettingsUpdate(Parsable):
    """
    Request body for `PATCH job/export/ifc/settings`. Only the settings present in thebody are changed; every setting left out keeps its current value. The change is written tothe settings file SPACE GASS reads.
    """
    # Include the analytical model — the analysis idealisation of the structure: its members,plates, loads and load combinations.
    analytical_model: Optional[bool] = None
    # The program an IFC export is written for. SPACE GASS section names are translated to thatprogram's naming through the built-in conversion tables, and a few writers change shape forit (the file header for Tekla Structural, member naming for Revit Structure).
    convert_to: Optional[IfcConvertTo] = None
    # Include the physical model — the fabricated shape of the structure: its members andplates as solids.
    physical_model: Optional[bool] = None
    # IFC schema an export is written against.
    schema: Optional[IfcSchema] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IfcExportSettingsUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IfcExportSettingsUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IfcExportSettingsUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ifc_convert_to import IfcConvertTo
        from .ifc_schema import IfcSchema

        from .ifc_convert_to import IfcConvertTo
        from .ifc_schema import IfcSchema

        fields: dict[str, Callable[[Any], None]] = {
            "analyticalModel": lambda n : setattr(self, 'analytical_model', n.get_bool_value()),
            "convertTo": lambda n : setattr(self, 'convert_to', n.get_enum_value(IfcConvertTo)),
            "physicalModel": lambda n : setattr(self, 'physical_model', n.get_bool_value()),
            "schema": lambda n : setattr(self, 'schema', n.get_enum_value(IfcSchema)),
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
        writer.write_bool_value("analyticalModel", self.analytical_model)
        writer.write_enum_value("convertTo", self.convert_to)
        writer.write_bool_value("physicalModel", self.physical_model)
        writer.write_enum_value("schema", self.schema)
    

