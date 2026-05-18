from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union, overload
from warnings import warn

if TYPE_CHECKING:
    from ......models.error_response import ErrorResponse
    from ......models.plate_nodal_force_query_result import PlateNodalForceQueryResult
    from .metadata.metadata_request_builder import MetadataRequestBuilder

class PlateNodalForcesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/static/plate-nodal-forces
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PlateNodalForcesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/static/plate-nodal-forces{?Limit*,Offset*,cases*,plates*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        cases: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        plates: Optional[str] = None,
    ) -> Optional[PlateNodalForceQueryResult]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[PlateNodalForcesRequestBuilderGetQueryParameters]] = None) -> Optional[PlateNodalForceQueryResult]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[PlateNodalForcesRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[PlateNodalForceQueryResult]:
        """
        Gets nodal force results for plates, grouped by load case and plate.Each result contains force values at each node of the plate element.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PlateNodalForceQueryResult]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "404": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.plate_nodal_force_query_result import PlateNodalForceQueryResult

        return await self.request_adapter.send_async(request_info, PlateNodalForceQueryResult, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PlateNodalForcesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets nodal force results for plates, grouped by load case and plate.Each result contains force values at each node of the plate element.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> PlateNodalForcesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PlateNodalForcesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PlateNodalForcesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PlateNodalForcesRequestBuilderGetQueryParameters():
        """
        Gets nodal force results for plates, grouped by load case and plate.Each result contains force values at each node of the plate element.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "limit":
                return "Limit"
            if original_name == "offset":
                return "Offset"
            if original_name == "cases":
                return "cases"
            if original_name == "plates":
                return "plates"
            return original_name
        
        # Load case Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all.
        cases: Optional[str] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Plate Ids in SG list format (e.g. `"1,3-7,10"`). Omit to return all.
        plates: Optional[str] = None

    
    @dataclass
    class PlateNodalForcesRequestBuilderGetRequestConfiguration(RequestConfiguration[PlateNodalForcesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

