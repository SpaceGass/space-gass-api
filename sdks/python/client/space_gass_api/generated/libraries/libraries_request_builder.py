from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .materials.materials_request_builder import MaterialsRequestBuilder
    from .sections.sections_request_builder import SectionsRequestBuilder
    from .vehicles.vehicles_request_builder import VehiclesRequestBuilder

class LibrariesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /libraries
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LibrariesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/libraries", path_parameters)
    
    @property
    def materials(self) -> MaterialsRequestBuilder:
        """
        The materials property
        """
        from .materials.materials_request_builder import MaterialsRequestBuilder

        return MaterialsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sections(self) -> SectionsRequestBuilder:
        """
        The sections property
        """
        from .sections.sections_request_builder import SectionsRequestBuilder

        return SectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vehicles(self) -> VehiclesRequestBuilder:
        """
        The vehicles property
        """
        from .vehicles.vehicles_request_builder import VehiclesRequestBuilder

        return VehiclesRequestBuilder(self.request_adapter, self.path_parameters)
    

