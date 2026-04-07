from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .element_forces.element_forces_request_builder import ElementForcesRequestBuilder
    from .element_stresses.element_stresses_request_builder import ElementStressesRequestBuilder
    from .nodal_forces.nodal_forces_request_builder import NodalForcesRequestBuilder

class PlateRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/static/plate
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PlateRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/static/plate", path_parameters)
    
    @property
    def element_forces(self) -> ElementForcesRequestBuilder:
        """
        The elementForces property
        """
        from .element_forces.element_forces_request_builder import ElementForcesRequestBuilder

        return ElementForcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def element_stresses(self) -> ElementStressesRequestBuilder:
        """
        The elementStresses property
        """
        from .element_stresses.element_stresses_request_builder import ElementStressesRequestBuilder

        return ElementStressesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def nodal_forces(self) -> NodalForcesRequestBuilder:
        """
        The nodalForces property
        """
        from .nodal_forces.nodal_forces_request_builder import NodalForcesRequestBuilder

        return NodalForcesRequestBuilder(self.request_adapter, self.path_parameters)
    

