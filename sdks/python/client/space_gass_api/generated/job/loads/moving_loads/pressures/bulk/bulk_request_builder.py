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
    from ......models.bulk_deleted_bulk_result import BulkDeletedBulkResult
    from ......models.error_response import ErrorResponse
    from ......models.moving_load_pressure_bulk_result import MovingLoadPressureBulkResult
    from ......models.moving_load_pressure_create import MovingLoadPressureCreate
    from ......models.moving_load_pressure_update import MovingLoadPressureUpdate

class BulkRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/moving-loads/pressures/bulk
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new BulkRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/moving-loads/pressures/bulk{?continueOnError*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def delete(
        self,
        body: list[int],
        *,
        continue_on_error: Optional[bool] = None,
    ) -> Optional[BulkDeletedBulkResult]: ...
    @overload
    async def delete(self, body: list[int], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderDeleteQueryParameters]] = None) -> Optional[BulkDeletedBulkResult]: ...
    # --- end overloads ---
    async def delete(self,body: list[int], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderDeleteQueryParameters]] = None, **kwargs) -> Optional[BulkDeletedBulkResult]:
        """
        Deletes multiple catalog items by Id. The body is a JSON array of integer Ids(e.g. `[1, 5, 10]`). An item referenced by a scenario load fails with an in-use errorrather than being deleted.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BulkDeletedBulkResult]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_delete_request_information(
            body, request_configuration
        )
        from ......models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.bulk_deleted_bulk_result import BulkDeletedBulkResult

        return await self.request_adapter.send_async(request_info, BulkDeletedBulkResult, error_mapping)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def patch(
        self,
        body: list[MovingLoadPressureUpdate],
        *,
        continue_on_error: Optional[bool] = None,
    ) -> Optional[MovingLoadPressureBulkResult]: ...
    @overload
    async def patch(self, body: list[MovingLoadPressureUpdate], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderPatchQueryParameters]] = None) -> Optional[MovingLoadPressureBulkResult]: ...
    # --- end overloads ---
    async def patch(self,body: list[MovingLoadPressureUpdate], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderPatchQueryParameters]] = None, **kwargs) -> Optional[MovingLoadPressureBulkResult]:
        """
        Partially updates multiple catalog items in one call; each body item carries the `id`of the item to update. They persist with a single save.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MovingLoadPressureBulkResult]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.moving_load_pressure_bulk_result import MovingLoadPressureBulkResult

        return await self.request_adapter.send_async(request_info, MovingLoadPressureBulkResult, error_mapping)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def post(
        self,
        body: list[MovingLoadPressureCreate],
        *,
        continue_on_error: Optional[bool] = None,
    ) -> Optional[MovingLoadPressureBulkResult]: ...
    @overload
    async def post(self, body: list[MovingLoadPressureCreate], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderPostQueryParameters]] = None) -> Optional[MovingLoadPressureBulkResult]: ...
    # --- end overloads ---
    async def post(self,body: list[MovingLoadPressureCreate], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderPostQueryParameters]] = None, **kwargs) -> Optional[MovingLoadPressureBulkResult]:
        """
        Creates multiple catalog items in one call; they persist with a single save.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MovingLoadPressureBulkResult]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.moving_load_pressure_bulk_result import MovingLoadPressureBulkResult

        return await self.request_adapter.send_async(request_info, MovingLoadPressureBulkResult, error_mapping)
    
    def to_delete_request_information(self,body: list[int], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        Deletes multiple catalog items by Id. The body is a JSON array of integer Ids(e.g. `[1, 5, 10]`). An item referenced by a scenario load fails with an in-use errorrather than being deleted.
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
    
    def to_patch_request_information(self,body: list[MovingLoadPressureUpdate], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderPatchQueryParameters]] = None) -> RequestInformation:
        """
        Partially updates multiple catalog items in one call; each body item carries the `id`of the item to update. They persist with a single save.
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
    
    def to_post_request_information(self,body: list[MovingLoadPressureCreate], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Creates multiple catalog items in one call; they persist with a single save.
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
        Deletes multiple catalog items by Id. The body is a JSON array of integer Ids(e.g. `[1, 5, 10]`). An item referenced by a scenario load fails with an in-use errorrather than being deleted.
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
    class BulkRequestBuilderDeleteRequestConfiguration(RequestConfiguration[BulkRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class BulkRequestBuilderPatchQueryParameters():
        """
        Partially updates multiple catalog items in one call; each body item carries the `id`of the item to update. They persist with a single save.
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
        Creates multiple catalog items in one call; they persist with a single save.
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
    

