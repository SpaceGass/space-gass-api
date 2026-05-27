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
    from .....models.error_response import ErrorResponse
    from .....models.expand_option import ExpandOption
    from .....models.load_case import LoadCase
    from .....models.load_case_update import LoadCaseUpdate

class LoadCasesItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/load-cases/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LoadCasesItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/load-cases/{id}{?Expand*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Removes the title, notes and metadata for the load case. Does not delete the actualloads assigned to the case or its combination items — the case may still appear inlistings if it has loads assigned to it.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ErrorResponse,
            "404": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        expand: Optional[ExpandOption] = None,
    ) -> Optional[LoadCase]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[LoadCasesItemRequestBuilderGetQueryParameters]] = None) -> Optional[LoadCase]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[LoadCasesItemRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[LoadCase]:
        """
        Gets a single load case by Id. `Expand` defaults to `all`, which hydrates`combinationItems` for combination cases; pass `Expand=none` to suppress.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LoadCase]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ErrorResponse,
            "404": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.load_case import LoadCase

        return await self.request_adapter.send_async(request_info, LoadCase, error_mapping)
    
    async def patch(self,body: LoadCaseUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[LoadCase]:
        """
        Partially updates a load case (title, notes). Only fields supplied in the body arechanged; omitted fields are left as-is.
        param body: DTO for updating an existing load case.All fields are optional to support partial updates.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LoadCase]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.load_case import LoadCase

        return await self.request_adapter.send_async(request_info, LoadCase, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Removes the title, notes and metadata for the load case. Does not delete the actualloads assigned to the case or its combination items — the case may still appear inlistings if it has loads assigned to it.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[LoadCasesItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets a single load case by Id. `Expand` defaults to `all`, which hydrates`combinationItems` for combination cases; pass `Expand=none` to suppress.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: LoadCaseUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Partially updates a load case (title, notes). Only fields supplied in the body arechanged; omitted fields are left as-is.
        param body: DTO for updating an existing load case.All fields are optional to support partial updates.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> LoadCasesItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LoadCasesItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return LoadCasesItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class LoadCasesItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class LoadCasesItemRequestBuilderGetQueryParameters():
        """
        Gets a single load case by Id. `Expand` defaults to `all`, which hydrates`combinationItems` for combination cases; pass `Expand=none` to suppress.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "Expand"
            return original_name
        
        # Sub-resource expansion. Defaults to `all`.
        expand: Optional[ExpandOption] = None

    
    @dataclass
    class LoadCasesItemRequestBuilderGetRequestConfiguration(RequestConfiguration[LoadCasesItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class LoadCasesItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

