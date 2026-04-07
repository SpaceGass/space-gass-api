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
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .......models.plate_stress_query_result import PlateStressQueryResult
    from .......models.problem_details import ProblemDetails

class ElementStressesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/query/analysis/static/plate/element-stresses
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ElementStressesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/query/analysis/static/plate/element-stresses{?Limit*,Offset*,case*,plate*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ElementStressesRequestBuilderGetQueryParameters]] = None) -> Optional[PlateStressQueryResult]:
        """
        Gets element stress results for plates, optionally filtered by load cases and plate keys.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PlateStressQueryResult]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.plate_stress_query_result import PlateStressQueryResult

        return await self.request_adapter.send_async(request_info, PlateStressQueryResult, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ElementStressesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets element stress results for plates, optionally filtered by load cases and plate keys.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ElementStressesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ElementStressesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ElementStressesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ElementStressesRequestBuilderGetQueryParameters():
        """
        Gets element stress results for plates, optionally filtered by load cases and plate keys.
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
            if original_name == "case":
                return "case"
            if original_name == "plate":
                return "plate"
            return original_name
        
        # Filter by load case IDs.
        case: Optional[list[int]] = None

        # Maximum number of items to return. Default is null (return all).
        limit: Optional[int] = None

        # Number of items to skip from the start of the result set. Default is 0.
        offset: Optional[int] = None

        # Filter by plate keys.
        plate: Optional[list[int]] = None

    
    @dataclass
    class ElementStressesRequestBuilderGetRequestConfiguration(RequestConfiguration[ElementStressesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

