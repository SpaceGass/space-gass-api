from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .loading_type import LoadingType
    from .matrix_type import MatrixType
    from .non_linear_theory import NonLinearTheory
    from .optimization_axis import OptimizationAxis
    from .optimization_method import OptimizationMethod
    from .plate_type import PlateType
    from .solver_type import SolverType
    from .tension_compression_only_mode import TensionCompressionOnlyMode

@dataclass
class StaticSettingsUpdate(Parsable):
    """
    Update request for Static Analysis settings.Only fields included in the request are updated; omit a field to keep its current value.Used by PATCH /static/settings and the POST run endpoints.
    """
    # The checkNonExistentCases property
    check_non_existent_cases: Optional[bool] = None
    # The convergenceAccuracy property
    convergence_accuracy: Optional[float] = None
    # The dampingFactor property
    damping_factor: Optional[float] = None
    # The dampingSteps property
    damping_steps: Optional[int] = None
    # The deflectionsConvergence property
    deflections_convergence: Optional[bool] = None
    # The drillingStiffness property
    drilling_stiffness: Optional[float] = None
    # The frameBucklingCheck property
    frame_buckling_check: Optional[bool] = None
    # The loadCases property
    load_cases: Optional[str] = None
    # The loadStepIterations property
    load_step_iterations: Optional[int] = None
    # The loadSteps property
    load_steps: Optional[int] = None
    # Loading type for non-linear static analysis.Only used for non-linear static analysis.
    loading: Optional[LoadingType] = None
    # Stiffness matrix type for non-linear static analysis.Only used for non-linear static analysis.
    matrix_type: Optional[MatrixType] = None
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
    # The pDeltaBig property
    p_delta_big: Optional[bool] = None
    # The pDeltaSmall property
    p_delta_small: Optional[bool] = None
    # Plate element formulation type.
    plate_type: Optional[PlateType] = None
    # The residualsConvergence property
    residuals_convergence: Optional[bool] = None
    # The retainCases property
    retain_cases: Optional[bool] = None
    # The reversalIterations property
    reversal_iterations: Optional[int] = None
    # The rotateLocalLoads property
    rotate_local_loads: Optional[bool] = None
    # Matrix solver type used by the analysis engine.Integer values mirror SPACE GASS's `SGSolverType` enum(NetCommon/CommonEnums.vb): 0=Pardiso, 1=Wavefront, 2=Watcom (legacy,not exposed), 3=SG-X (cloud, dispatched externally — not yet supportedby the in-process API analysis path).
    solver_type: Optional[SolverType] = None
    # The stabilizeUnrestrainedNodes property
    stabilize_unrestrained_nodes: Optional[bool] = None
    # Controls how tension-only and compression-only members are handled during analysis.
    tension_compression_only: Optional[TensionCompressionOnlyMode] = None
    # Non-linear static analysis theory type.Only used for non-linear static analysis.
    theory: Optional[NonLinearTheory] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StaticSettingsUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StaticSettingsUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StaticSettingsUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .loading_type import LoadingType
        from .matrix_type import MatrixType
        from .non_linear_theory import NonLinearTheory
        from .optimization_axis import OptimizationAxis
        from .optimization_method import OptimizationMethod
        from .plate_type import PlateType
        from .solver_type import SolverType
        from .tension_compression_only_mode import TensionCompressionOnlyMode

        from .loading_type import LoadingType
        from .matrix_type import MatrixType
        from .non_linear_theory import NonLinearTheory
        from .optimization_axis import OptimizationAxis
        from .optimization_method import OptimizationMethod
        from .plate_type import PlateType
        from .solver_type import SolverType
        from .tension_compression_only_mode import TensionCompressionOnlyMode

        fields: dict[str, Callable[[Any], None]] = {
            "checkNonExistentCases": lambda n : setattr(self, 'check_non_existent_cases', n.get_bool_value()),
            "convergenceAccuracy": lambda n : setattr(self, 'convergence_accuracy', n.get_float_value()),
            "dampingFactor": lambda n : setattr(self, 'damping_factor', n.get_float_value()),
            "dampingSteps": lambda n : setattr(self, 'damping_steps', n.get_int_value()),
            "deflectionsConvergence": lambda n : setattr(self, 'deflections_convergence', n.get_bool_value()),
            "drillingStiffness": lambda n : setattr(self, 'drilling_stiffness', n.get_float_value()),
            "frameBucklingCheck": lambda n : setattr(self, 'frame_buckling_check', n.get_bool_value()),
            "loadCases": lambda n : setattr(self, 'load_cases', n.get_str_value()),
            "loadStepIterations": lambda n : setattr(self, 'load_step_iterations', n.get_int_value()),
            "loadSteps": lambda n : setattr(self, 'load_steps', n.get_int_value()),
            "loading": lambda n : setattr(self, 'loading', n.get_enum_value(LoadingType)),
            "matrixType": lambda n : setattr(self, 'matrix_type', n.get_enum_value(MatrixType)),
            "optimizationAxis": lambda n : setattr(self, 'optimization_axis', n.get_enum_value(OptimizationAxis)),
            "optimizationMethod": lambda n : setattr(self, 'optimization_method', n.get_enum_value(OptimizationMethod)),
            "optimizationX": lambda n : setattr(self, 'optimization_x', n.get_float_value()),
            "optimizationY": lambda n : setattr(self, 'optimization_y', n.get_float_value()),
            "optimizationZ": lambda n : setattr(self, 'optimization_z', n.get_float_value()),
            "pDeltaBig": lambda n : setattr(self, 'p_delta_big', n.get_bool_value()),
            "pDeltaSmall": lambda n : setattr(self, 'p_delta_small', n.get_bool_value()),
            "plateType": lambda n : setattr(self, 'plate_type', n.get_enum_value(PlateType)),
            "residualsConvergence": lambda n : setattr(self, 'residuals_convergence', n.get_bool_value()),
            "retainCases": lambda n : setattr(self, 'retain_cases', n.get_bool_value()),
            "reversalIterations": lambda n : setattr(self, 'reversal_iterations', n.get_int_value()),
            "rotateLocalLoads": lambda n : setattr(self, 'rotate_local_loads', n.get_bool_value()),
            "solverType": lambda n : setattr(self, 'solver_type', n.get_enum_value(SolverType)),
            "stabilizeUnrestrainedNodes": lambda n : setattr(self, 'stabilize_unrestrained_nodes', n.get_bool_value()),
            "tensionCompressionOnly": lambda n : setattr(self, 'tension_compression_only', n.get_enum_value(TensionCompressionOnlyMode)),
            "theory": lambda n : setattr(self, 'theory', n.get_enum_value(NonLinearTheory)),
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
        writer.write_float_value("convergenceAccuracy", self.convergence_accuracy)
        writer.write_float_value("dampingFactor", self.damping_factor)
        writer.write_int_value("dampingSteps", self.damping_steps)
        writer.write_bool_value("deflectionsConvergence", self.deflections_convergence)
        writer.write_float_value("drillingStiffness", self.drilling_stiffness)
        writer.write_bool_value("frameBucklingCheck", self.frame_buckling_check)
        writer.write_str_value("loadCases", self.load_cases)
        writer.write_int_value("loadStepIterations", self.load_step_iterations)
        writer.write_int_value("loadSteps", self.load_steps)
        writer.write_enum_value("loading", self.loading)
        writer.write_enum_value("matrixType", self.matrix_type)
        writer.write_enum_value("optimizationAxis", self.optimization_axis)
        writer.write_enum_value("optimizationMethod", self.optimization_method)
        writer.write_float_value("optimizationX", self.optimization_x)
        writer.write_float_value("optimizationY", self.optimization_y)
        writer.write_float_value("optimizationZ", self.optimization_z)
        writer.write_bool_value("pDeltaBig", self.p_delta_big)
        writer.write_bool_value("pDeltaSmall", self.p_delta_small)
        writer.write_enum_value("plateType", self.plate_type)
        writer.write_bool_value("residualsConvergence", self.residuals_convergence)
        writer.write_bool_value("retainCases", self.retain_cases)
        writer.write_int_value("reversalIterations", self.reversal_iterations)
        writer.write_bool_value("rotateLocalLoads", self.rotate_local_loads)
        writer.write_enum_value("solverType", self.solver_type)
        writer.write_bool_value("stabilizeUnrestrainedNodes", self.stabilize_unrestrained_nodes)
        writer.write_enum_value("tensionCompressionOnly", self.tension_compression_only)
        writer.write_enum_value("theory", self.theory)
    

