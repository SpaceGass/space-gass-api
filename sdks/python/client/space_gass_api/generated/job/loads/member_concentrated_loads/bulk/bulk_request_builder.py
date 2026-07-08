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
    from .....models.member_concentrated_load_bulk_result import MemberConcentratedLoadBulkResult
    from .....models.member_concentrated_load_create import MemberConcentratedLoadCreate
    from .....models.member_concentrated_load_key import MemberConcentratedLoadKey
    from .....models.member_concentrated_load_key_bulk_result import MemberConcentratedLoadKeyBulkResult
    from .....models.member_concentrated_load_update import MemberConcentratedLoadUpdate

class BulkRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/loads/member-concentrated-loads/bulk
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new BulkRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/loads/member-concentrated-loads/bulk{?continueOnError*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def delete(
        self,
        body: list[MemberConcentratedLoadKey],
        *,
        continue_on_error: Optional[bool] = None,
    ) -> Optional[MemberConcentratedLoadKeyBulkResult]: ...
    @overload
    async def delete(self, body: list[MemberConcentratedLoadKey], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderDeleteQueryParameters]] = None) -> Optional[MemberConcentratedLoadKeyBulkResult]: ...
    # --- end overloads ---
    async def delete(self,body: list[MemberConcentratedLoadKey], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderDeleteQueryParameters]] = None, **kwargs) -> Optional[MemberConcentratedLoadKeyBulkResult]:
        """
        Deletes multiple member concentrated loads. Case, member, and subLoad are all required for each entry.The succeeded array echoes back the Ids of each successfully deleted load.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MemberConcentratedLoadKeyBulkResult]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_delete_request_information(
            body, request_configuration
        )
        from .....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.member_concentrated_load_key_bulk_result import MemberConcentratedLoadKeyBulkResult

        return await self.request_adapter.send_async(request_info, MemberConcentratedLoadKeyBulkResult, error_mapping)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def patch(
        self,
        body: list[MemberConcentratedLoadUpdate],
        *,
        continue_on_error: Optional[bool] = None,
    ) -> Optional[MemberConcentratedLoadBulkResult]: ...
    @overload
    async def patch(self, body: list[MemberConcentratedLoadUpdate], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderPatchQueryParameters]] = None) -> Optional[MemberConcentratedLoadBulkResult]: ...
    # --- end overloads ---
    async def patch(self,body: list[MemberConcentratedLoadUpdate], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderPatchQueryParameters]] = None, **kwargs) -> Optional[MemberConcentratedLoadBulkResult]:
        """
        Updates multiple member concentrated loads. Each item must include case, member, and subLoad in the body.All load cases referenced must be Primary.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MemberConcentratedLoadBulkResult]
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
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.member_concentrated_load_bulk_result import MemberConcentratedLoadBulkResult

        return await self.request_adapter.send_async(request_info, MemberConcentratedLoadBulkResult, error_mapping)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def post(
        self,
        body: list[MemberConcentratedLoadCreate],
        *,
        continue_on_error: Optional[bool] = None,
    ) -> Optional[MemberConcentratedLoadBulkResult]: ...
    @overload
    async def post(self, body: list[MemberConcentratedLoadCreate], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderPostQueryParameters]] = None) -> Optional[MemberConcentratedLoadBulkResult]: ...
    # --- end overloads ---
    async def post(self,body: list[MemberConcentratedLoadCreate], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderPostQueryParameters]] = None, **kwargs) -> Optional[MemberConcentratedLoadBulkResult]:
        """
        Creates multiple loads in a bulk operation.All load cases referenced must exist and be Primary load cases.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MemberConcentratedLoadBulkResult]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.member_concentrated_load_bulk_result import MemberConcentratedLoadBulkResult

        return await self.request_adapter.send_async(request_info, MemberConcentratedLoadBulkResult, error_mapping)
    
    def to_delete_request_information(self,body: list[MemberConcentratedLoadKey], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        Deletes multiple member concentrated loads. Case, member, and subLoad are all required for each entry.The succeeded array echoes back the Ids of each successfully deleted load.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def to_patch_request_information(self,body: list[MemberConcentratedLoadUpdate], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderPatchQueryParameters]] = None) -> RequestInformation:
        """
        Updates multiple member concentrated loads. Each item must include case, member, and subLoad in the body.All load cases referenced must be Primary.
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
    
    def to_post_request_information(self,body: list[MemberConcentratedLoadCreate], request_configuration: Optional[RequestConfiguration[BulkRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Creates multiple loads in a bulk operation.All load cases referenced must exist and be Primary load cases.
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
        Deletes multiple member concentrated loads. Case, member, and subLoad are all required for each entry.The succeeded array echoes back the Ids of each successfully deleted load.
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
        Updates multiple member concentrated loads. Each item must include case, member, and subLoad in the body.All load cases referenced must be Primary.
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
        Creates multiple loads in a bulk operation.All load cases referenced must exist and be Primary load cases.
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
    

