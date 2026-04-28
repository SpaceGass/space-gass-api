from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .axial_force_distribution import AxialForceDistribution
    from .buckling_theory import BucklingTheory
    from .optimization_axis import OptimizationAxis
    from .optimization_method import OptimizationMethod
    from .plate_type import PlateType
    from .solver_type import SolverType
    from .tension_compression_only_mode import TensionCompressionOnlyMode

@dataclass
class BucklingSettingsUpdate(Parsable):
    """
    Update request for Buckling Analysis settings.Only fields included in the request are updated; omit a field to keep its current value.
    """
    # Axial force distribution method for buckling analysis.
    axial_force_distribution: Optional[AxialForceDistribution] = None
    # The checkNonExistentCases property
    check_non_existent_cases: Optional[bool] = None
    # The drillingStiffness property
    drilling_stiffness: Optional[float] = None
    # The extraIterations property
    extra_iterations: Optional[bool] = None
    # The loadCases property
    load_cases: Optional[str] = None
    # The lowerLimit property
    lower_limit: Optional[float] = None
    # The modes property
    modes: Optional[int] = None
    # Axis used for optimization in analysis.
    optimization_axis: Optional[OptimizationAxis] = None
    # Optimization method for analysis.
    optimization_method: Optional[OptimizationMethod] = None
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
    # The reversalIterations property
    reversal_iterations: Optional[int] = None
    # Matrix solver type used by the analysis engine.
    solver_type: Optional[SolverType] = None
    # The stabilizeUnrestrainedNodes property
    stabilize_unrestrained_nodes: Optional[bool] = None
    # Controls how tension-only and compression-only members are handled during analysis.
    tension_compression_only: Optional[TensionCompressionOnlyMode] = None
    # Eigensolver theory used for buckling analysis.
    theory: Optional[BucklingTheory] = None
    # The tolerance property
    tolerance: Optional[float] = None
    # The upperLimit property
    upper_limit: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BucklingSettingsUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BucklingSettingsUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BucklingSettingsUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .axial_force_distribution import AxialForceDistribution
        from .buckling_theory import BucklingTheory
        from .optimization_axis import OptimizationAxis
        from .optimization_method import OptimizationMethod
        from .plate_type import PlateType
        from .solver_type import SolverType
        from .tension_compression_only_mode import TensionCompressionOnlyMode

        from .axial_force_distribution import AxialForceDistribution
        from .buckling_theory import BucklingTheory
        from .optimization_axis import OptimizationAxis
        from .optimization_method import OptimizationMethod
        from .plate_type import PlateType
        from .solver_type import SolverType
        from .tension_compression_only_mode import TensionCompressionOnlyMode

        fields: dict[str, Callable[[Any], None]] = {
            "axialForceDistribution": lambda n : setattr(self, 'axial_force_distribution', n.get_enum_value(AxialForceDistribution)),
            "checkNonExistentCases": lambda n : setattr(self, 'check_non_existent_cases', n.get_bool_value()),
            "drillingStiffness": lambda n : setattr(self, 'drilling_stiffness', n.get_float_value()),
            "extraIterations": lambda n : setattr(self, 'extra_iterations', n.get_bool_value()),
            "loadCases": lambda n : setattr(self, 'load_cases', n.get_str_value()),
            "lowerLimit": lambda n : setattr(self, 'lower_limit', n.get_float_value()),
            "modes": lambda n : setattr(self, 'modes', n.get_int_value()),
            "optimizationAxis": lambda n : setattr(self, 'optimization_axis', n.get_enum_value(OptimizationAxis)),
            "optimizationMethod": lambda n : setattr(self, 'optimization_method', n.get_enum_value(OptimizationMethod)),
            "optimizationX": lambda n : setattr(self, 'optimization_x', n.get_float_value()),
            "optimizationY": lambda n : setattr(self, 'optimization_y', n.get_float_value()),
            "optimizationZ": lambda n : setattr(self, 'optimization_z', n.get_float_value()),
            "plateType": lambda n : setattr(self, 'plate_type', n.get_enum_value(PlateType)),
            "retainCases": lambda n : setattr(self, 'retain_cases', n.get_bool_value()),
            "reversalIterations": lambda n : setattr(self, 'reversal_iterations', n.get_int_value()),
            "solverType": lambda n : setattr(self, 'solver_type', n.get_enum_value(SolverType)),
            "stabilizeUnrestrainedNodes": lambda n : setattr(self, 'stabilize_unrestrained_nodes', n.get_bool_value()),
            "tensionCompressionOnly": lambda n : setattr(self, 'tension_compression_only', n.get_enum_value(TensionCompressionOnlyMode)),
            "theory": lambda n : setattr(self, 'theory', n.get_enum_value(BucklingTheory)),
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
        writer.write_enum_value("axialForceDistribution", self.axial_force_distribution)
        writer.write_bool_value("checkNonExistentCases", self.check_non_existent_cases)
        writer.write_float_value("drillingStiffness", self.drilling_stiffness)
        writer.write_bool_value("extraIterations", self.extra_iterations)
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
        writer.write_int_value("reversalIterations", self.reversal_iterations)
        writer.write_enum_value("solverType", self.solver_type)
        writer.write_bool_value("stabilizeUnrestrainedNodes", self.stabilize_unrestrained_nodes)
        writer.write_enum_value("tensionCompressionOnly", self.tension_compression_only)
        writer.write_enum_value("theory", self.theory)
        writer.write_float_value("tolerance", self.tolerance)
        writer.write_float_value("upperLimit", self.upper_limit)
    

