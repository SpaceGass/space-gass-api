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
    from .....models.error_response import ErrorResponse
    from .....models.load_category_bulk_result import LoadCategoryBulkResult
    from .....models.load_category_create import LoadCategoryCreate
    from .....models.load_category_update import LoadCategoryUpdate
    from .....models.object_bulk_result import ObjectBulkResult

class BulkRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/load-categories/bulk
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new BulkRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/load-categories/bulk{?continueOnError*}", path_parameters)
    
    async def delete(self,body: list[int], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderDeleteQueryParameters]] = None) -> Optional[ObjectBulkResult]:
        """
        Deletes multiple entities by Id. The body is a JSON array of integer Ids(e.g. `[1, 5, 10]`) — consistent with every other bulk-delete endpointin the API (see CLAUDE.md "Query Parameter Conventions").
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ObjectBulkResult]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_delete_request_information(
            body, request_configuration
        )
        from .....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "404": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.object_bulk_result import ObjectBulkResult

        return await self.request_adapter.send_async(request_info, ObjectBulkResult, error_mapping)
    
    async def patch(self,body: list[LoadCategoryUpdate], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderPatchQueryParameters]] = None) -> Optional[LoadCategoryBulkResult]:
        """
        Updates multiple items in a bulk operation.Each item must include its Id in the request body.If a validator is registered, all items are validated upfront before any are updated.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LoadCategoryBulkResult]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "404": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.load_category_bulk_result import LoadCategoryBulkResult

        return await self.request_adapter.send_async(request_info, LoadCategoryBulkResult, error_mapping)
    
    async def post(self,body: list[LoadCategoryCreate], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderPostQueryParameters]] = None) -> Optional[LoadCategoryBulkResult]:
        """
        Creates multiple items in a bulk operation.If a validator is registered, all items are validated upfront before any are created.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LoadCategoryBulkResult]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "404": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.load_category_bulk_result import LoadCategoryBulkResult

        return await self.request_adapter.send_async(request_info, LoadCategoryBulkResult, error_mapping)
    
    def to_delete_request_information(self,body: list[int], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        Deletes multiple entities by Id. The body is a JSON array of integer Ids(e.g. `[1, 5, 10]`) — consistent with every other bulk-delete endpointin the API (see CLAUDE.md "Query Parameter Conventions").
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_scalar(self.request_adapter, "application/json", body)
        return request_info
    
    def to_patch_request_information(self,body: list[LoadCategoryUpdate], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderPatchQueryParameters]] = None) -> RequestInformation:
        """
        Updates multiple items in a bulk operation.Each item must include its Id in the request body.If a validator is registered, all items are validated upfront before any are updated.
        param body: The request body
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
    
    def to_post_request_information(self,body: list[LoadCategoryCreate], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Creates multiple items in a bulk operation.If a validator is registered, all items are validated upfront before any are created.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> BulkRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: BulkRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return BulkRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class BulkRequestBuilderDeleteQueryParameters():
        """
        Deletes multiple entities by Id. The body is a JSON array of integer Ids(e.g. `[1, 5, 10]`) — consistent with every other bulk-delete endpointin the API (see CLAUDE.md "Query Parameter Conventions").
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "continue_on_error":
                return "continueOnError"
            return original_name
        
        # Whether to continue on error
        continue_on_error: Optional[bool] = None

    
    @dataclass
    class BulkRequestBuilderDeleteRequestConfiguration(RequestConfiguration[BulkRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class BulkRequestBuilderPatchQueryParameters():
        """
        Updates multiple items in a bulk operation.Each item must include its Id in the request body.If a validator is registered, all items are validated upfront before any are updated.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "continue_on_error":
                return "continueOnError"
            return original_name
        
        # Whether to continue processing after individual failures
        continue_on_error: Optional[bool] = None

    
    @dataclass
    class BulkRequestBuilderPatchRequestConfiguration(RequestConfiguration[BulkRequestBuilderPatchQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class BulkRequestBuilderPostQueryParameters():
        """
        Creates multiple items in a bulk operation.If a validator is registered, all items are validated upfront before any are created.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "continue_on_error":
                return "continueOnError"
            return original_name
        
        # Whether to continue processing after individual failures
        continue_on_error: Optional[bool] = None

    
    @dataclass
    class BulkRequestBuilderPostRequestConfiguration(RequestConfiguration[BulkRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

