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
    from ...models.api_mode import ApiMode
    from ...models.api_mode_update import ApiModeUpdate
    from ...models.error_response import ErrorResponse

class ModeRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /service/mode
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ModeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/service/mode", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ApiMode]:
        """
        Returns the current API mode and any pending transition (queuedwhile a job is open).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ApiMode]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.api_mode import ApiMode

        return await self.request_adapter.send_async(request_info, ApiMode, error_mapping)
    
    async def post(self,body: ApiModeUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ApiMode]:
        """
        Transitions the API between `readwrite` and `readonly`.When switching to `readonly` with a job open, the transitionis queued and returns 202 — the switch commits when the jobcloses. When switching to `readwrite` the API attempts tore-acquire MODULE_API_ID; a failure returns 409 and leaves themode unchanged.
        param body: Request body for `POST /service/mode`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ApiMode]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "409": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.api_mode import ApiMode

        return await self.request_adapter.send_async(request_info, ApiMode, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the current API mode and any pending transition (queuedwhile a job is open).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: ApiModeUpdate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Transitions the API between `readwrite` and `readonly`.When switching to `readonly` with a job open, the transitionis queued and returns 202 — the switch commits when the jobcloses. When switching to `readwrite` the API attempts tore-acquire MODULE_API_ID; a failure returns 409 and leaves themode unchanged.
        param body: Request body for `POST /service/mode`.
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
    
    def with_url(self,raw_url: str) -> ModeRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ModeRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ModeRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ModeRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ModeRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

