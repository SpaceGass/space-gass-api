from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .end_forces.end_forces_request_builder import EndForcesRequestBuilder
    from .intermediate_displacements.intermediate_displacements_request_builder import IntermediateDisplacementsRequestBuilder
    from .intermediate_forces.intermediate_forces_request_builder import IntermediateForcesRequestBuilder
    from .stresses.stresses_request_builder import StressesRequestBuilder

class MemberRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/static/member
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MemberRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/static/member", path_parameters)
    
    @property
    def end_forces(self) -> EndForcesRequestBuilder:
        """
        The endForces property
        """
        from .end_forces.end_forces_request_builder import EndForcesRequestBuilder

        return EndForcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def intermediate_displacements(self) -> IntermediateDisplacementsRequestBuilder:
        """
        The intermediateDisplacements property
        """
        from .intermediate_displacements.intermediate_displacements_request_builder import IntermediateDisplacementsRequestBuilder

        return IntermediateDisplacementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def intermediate_forces(self) -> IntermediateForcesRequestBuilder:
        """
        The intermediateForces property
        """
        from .intermediate_forces.intermediate_forces_request_builder import IntermediateForcesRequestBuilder

        return IntermediateForcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def stresses(self) -> StressesRequestBuilder:
        """
        The stresses property
        """
        from .stresses.stresses_request_builder import StressesRequestBuilder

        return StressesRequestBuilder(self.request_adapter, self.path_parameters)
    

