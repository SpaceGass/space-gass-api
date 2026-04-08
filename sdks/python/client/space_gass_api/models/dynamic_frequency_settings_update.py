from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .frequency_optimization_method import FrequencyOptimizationMethod
    from .optimization_axis import OptimizationAxis
    from .plate_type import PlateType
    from .solver_type import SolverType

@dataclass
class DynamicFrequencySettingsUpdate(Parsable):
    """
    Update DTO for Dynamic Frequency Analysis settings (PATCH semantics).All fields are nullable — only non-null fields are applied as overrides.
    """
    # The checkNonExistentCases property
    check_non_existent_cases: Optional[bool] = None
    # The drillingStiffness property
    drilling_stiffness: Optional[float] = None
    # The extraIterations property
    extra_iterations: Optional[bool] = None
    # The frequencyShift property
    frequency_shift: Optional[float] = None
    # The loadCases property
    load_cases: Optional[str] = None
    # The lowerLimit property
    lower_limit: Optional[float] = None
    # The modes property
    modes: Optional[int] = None
    # Axis used for optimization in analysis.
    optimization_axis: Optional[OptimizationAxis] = None
    # Optimization method for Dynamic Frequency analysis.Note: These have different integer mappings than the static/buckling OptimizationMethod enum.
    optimization_method: Optional[FrequencyOptimizationMethod] = None
    # The optimizationX property
    optimization_x: Optional[float] = None
    # The optimizationY property
    optimization_y: Optional[float] = None
    # The optimizationZ property
    optimization_z: Optional[float] = None
    # Plate element formulation type.
    plate_type: Optional[PlateType] = None
    # The retainCases property
    retain_cases: Optional[bool] = None
    # Matrix solver type used by the analysis engine.
    solver_type: Optional[SolverType] = None
    # The stabilizeUnrestrainedNodes property
    stabilize_unrestrained_nodes: Optional[bool] = None
    # The tolerance property
    tolerance: Optional[float] = None
    # The upperLimit property
    upper_limit: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DynamicFrequencySettingsUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DynamicFrequencySettingsUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DynamicFrequencySettingsUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .frequency_optimization_method import FrequencyOptimizationMethod
        from .optimization_axis import OptimizationAxis
        from .plate_type import PlateType
        from .solver_type import SolverType

        from .frequency_optimization_method import FrequencyOptimizationMethod
        from .optimization_axis import OptimizationAxis
        from .plate_type import PlateType
        from .solver_type import SolverType

        fields: dict[str, Callable[[Any], None]] = {
            "checkNonExistentCases": lambda n : setattr(self, 'check_non_existent_cases', n.get_bool_value()),
            "drillingStiffness": lambda n : setattr(self, 'drilling_stiffness', n.get_float_value()),
            "extraIterations": lambda n : setattr(self, 'extra_iterations', n.get_bool_value()),
            "frequencyShift": lambda n : setattr(self, 'frequency_shift', n.get_float_value()),
            "loadCases": lambda n : setattr(self, 'load_cases', n.get_str_value()),
            "lowerLimit": lambda n : setattr(self, 'lower_limit', n.get_float_value()),
            "modes": lambda n : setattr(self, 'modes', n.get_int_value()),
            "optimizationAxis": lambda n : setattr(self, 'optimization_axis', n.get_enum_value(OptimizationAxis)),
            "optimizationMethod": lambda n : setattr(self, 'optimization_method', n.get_enum_value(FrequencyOptimizationMethod)),
            "optimizationX": lambda n : setattr(self, 'optimization_x', n.get_float_value()),
            "optimizationY": lambda n : setattr(self, 'optimization_y', n.get_float_value()),
            "optimizationZ": lambda n : setattr(self, 'optimization_z', n.get_float_value()),
            "plateType": lambda n : setattr(self, 'plate_type', n.get_enum_value(PlateType)),
            "retainCases": lambda n : setattr(self, 'retain_cases', n.get_bool_value()),
            "solverType": lambda n : setattr(self, 'solver_type', n.get_enum_value(SolverType)),
            "stabilizeUnrestrainedNodes": lambda n : setattr(self, 'stabilize_unrestrained_nodes', n.get_bool_value()),
            "tolerance": lambda n : setattr(self, 'tolerance', n.get_float_value()),
            "upperLimit": lambda n : setattr(self, 'upper_limit', n.get_float_value()),
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
        writer.write_bool_value("checkNonExistentCases", self.check_non_existent_cases)
        writer.write_float_value("drillingStiffness", self.drilling_stiffness)
        writer.write_bool_value("extraIterations", self.extra_iterations)
        writer.write_float_value("frequencyShift", self.frequency_shift)
        writer.write_str_value("loadCases", self.load_cases)
        writer.write_float_value("lowerLimit", self.lower_limit)
        writer.write_int_value("modes", self.modes)
        writer.write_enum_value("optimizationAxis", self.optimization_axis)
        writer.write_enum_value("optimizationMethod", self.optimization_method)
        writer.write_float_value("optimizationX", self.optimization_x)
        writer.write_float_value("optimizationY", self.optimization_y)
        writer.write_float_value("optimizationZ", self.optimization_z)
        writer.write_enum_value("plateType", self.plate_type)
        writer.write_bool_value("retainCases", self.retain_cases)
        writer.write_enum_value("solverType", self.solver_type)
        writer.write_bool_value("stabilizeUnrestrainedNodes", self.stabilize_unrestrained_nodes)
        writer.write_float_value("tolerance", self.tolerance)
        writer.write_float_value("upperLimit", self.upper_limit)
    

