from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .combination_load_cases.combination_load_cases_request_builder import CombinationLoadCasesRequestBuilder
    from .load_cases.load_cases_request_builder import LoadCasesRequestBuilder
    from .load_case_groups.load_case_groups_request_builder import LoadCaseGroupsRequestBuilder
    from .load_categories.load_categories_request_builder import LoadCategoriesRequestBuilder
    from .lumped_mass_loads.lumped_mass_loads_request_builder import LumpedMassLoadsRequestBuilder
    from .member_concentrated_loads.member_concentrated_loads_request_builder import MemberConcentratedLoadsRequestBuilder
    from .member_distributed_loads.member_distributed_loads_request_builder import MemberDistributedLoadsRequestBuilder
    from .member_distributed_moments.member_distributed_moments_request_builder import MemberDistributedMomentsRequestBuilder
    from .member_prestress_loads.member_prestress_loads_request_builder import MemberPrestressLoadsRequestBuilder
    from .moving_loads.moving_loads_request_builder import MovingLoadsRequestBuilder
    from .node_displacements.node_displacements_request_builder import NodeDisplacementsRequestBuilder
    from .node_loads.node_loads_request_builder import NodeLoadsRequestBuilder
    from .plate_pressure_loads.plate_pressure_loads_request_builder import PlatePressureLoadsRequestBuilder
    from .self_weight_loads.self_weight_loads_request_builder import SelfWeightLoadsRequestBuilder
    from .thermal_loads.thermal_loads_request_builder import ThermalLoadsRequestBuilder

class LoadsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LoadsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads", path_parameters)
    
    @property
    def combination_load_cases(self) -> CombinationLoadCasesRequestBuilder:
        """
        The combinationLoadCases property
        """
        from .combination_load_cases.combination_load_cases_request_builder import CombinationLoadCasesRequestBuilder

        return CombinationLoadCasesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def load_case_groups(self) -> LoadCaseGroupsRequestBuilder:
        """
        The loadCaseGroups property
        """
        from .load_case_groups.load_case_groups_request_builder import LoadCaseGroupsRequestBuilder

        return LoadCaseGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def load_cases(self) -> LoadCasesRequestBuilder:
        """
        The loadCases property
        """
        from .load_cases.load_cases_request_builder import LoadCasesRequestBuilder

        return LoadCasesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def load_categories(self) -> LoadCategoriesRequestBuilder:
        """
        The loadCategories property
        """
        from .load_categories.load_categories_request_builder import LoadCategoriesRequestBuilder

        return LoadCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lumped_mass_loads(self) -> LumpedMassLoadsRequestBuilder:
        """
        The lumpedMassLoads property
        """
        from .lumped_mass_loads.lumped_mass_loads_request_builder import LumpedMassLoadsRequestBuilder

        return LumpedMassLoadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def member_concentrated_loads(self) -> MemberConcentratedLoadsRequestBuilder:
        """
        The memberConcentratedLoads property
        """
        from .member_concentrated_loads.member_concentrated_loads_request_builder import MemberConcentratedLoadsRequestBuilder

        return MemberConcentratedLoadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def member_distributed_loads(self) -> MemberDistributedLoadsRequestBuilder:
        """
        The memberDistributedLoads property
        """
        from .member_distributed_loads.member_distributed_loads_request_builder import MemberDistributedLoadsRequestBuilder

        return MemberDistributedLoadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def member_distributed_moments(self) -> MemberDistributedMomentsRequestBuilder:
        """
        The memberDistributedMoments property
        """
        from .member_distributed_moments.member_distributed_moments_request_builder import MemberDistributedMomentsRequestBuilder

        return MemberDistributedMomentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def member_prestress_loads(self) -> MemberPrestressLoadsRequestBuilder:
        """
        The memberPrestressLoads property
        """
        from .member_prestress_loads.member_prestress_loads_request_builder import MemberPrestressLoadsRequestBuilder

        return MemberPrestressLoadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def moving_loads(self) -> MovingLoadsRequestBuilder:
        """
        The movingLoads property
        """
        from .moving_loads.moving_loads_request_builder import MovingLoadsRequestBuilder

        return MovingLoadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def node_displacements(self) -> NodeDisplacementsRequestBuilder:
        """
        The nodeDisplacements property
        """
        from .node_displacements.node_displacements_request_builder import NodeDisplacementsRequestBuilder

        return NodeDisplacementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def node_loads(self) -> NodeLoadsRequestBuilder:
        """
        The nodeLoads property
        """
        from .node_loads.node_loads_request_builder import NodeLoadsRequestBuilder

        return NodeLoadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def plate_pressure_loads(self) -> PlatePressureLoadsRequestBuilder:
        """
        The platePressureLoads property
        """
        from .plate_pressure_loads.plate_pressure_loads_request_builder import PlatePressureLoadsRequestBuilder

        return PlatePressureLoadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def self_weight_loads(self) -> SelfWeightLoadsRequestBuilder:
        """
        The selfWeightLoads property
        """
        from .self_weight_loads.self_weight_loads_request_builder import SelfWeightLoadsRequestBuilder

        return SelfWeightLoadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def thermal_loads(self) -> ThermalLoadsRequestBuilder:
        """
        The thermalLoads property
        """
        from .thermal_loads.thermal_loads_request_builder import ThermalLoadsRequestBuilder

        return ThermalLoadsRequestBuilder(self.request_adapter, self.path_parameters)
    

