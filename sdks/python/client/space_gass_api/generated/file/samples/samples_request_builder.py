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
    from ...models.error_response import ErrorResponse
    from ...models.job_file_preview import JobFilePreview

class SamplesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /file/samples
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SamplesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/file/samples{?includeImages*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        include_images: Optional[bool] = None,
    ) -> Optional[list[JobFilePreview]]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[SamplesRequestBuilderGetQueryParameters]] = None) -> Optional[list[JobFilePreview]]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[SamplesRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[list[JobFilePreview]]:
        """
        Returns all available SPACE GASS sample project files.Each sample includes metadata and an optional preview image.The file paths use virtual `samples://` scheme (e.g. "samples://Portal Frame.SG")which can be used with the preview and open endpoints.            Samples are opened as new unsaved jobs — use Save As to persist changes.            Example usage with curl:                curl -X GET "/api/v1/file/samples?includeImages=true"
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[JobFilePreview]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.job_file_preview import JobFilePreview

        return await self.request_adapter.send_collection_async(request_info, JobFilePreview, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SamplesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns all available SPACE GASS sample project files.Each sample includes metadata and an optional preview image.The file paths use virtual `samples://` scheme (e.g. "samples://Portal Frame.SG")which can be used with the preview and open endpoints.            Samples are opened as new unsaved jobs — use Save As to persist changes.            Example usage with curl:                curl -X GET "/api/v1/file/samples?includeImages=true"
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> SamplesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SamplesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SamplesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SamplesRequestBuilderGetQueryParameters():
        """
        Returns all available SPACE GASS sample project files.Each sample includes metadata and an optional preview image.The file paths use virtual `samples://` scheme (e.g. "samples://Portal Frame.SG")which can be used with the preview and open endpoints.            Samples are opened as new unsaved jobs — use Save As to persist changes.            Example usage with curl:                curl -X GET "/api/v1/file/samples?includeImages=true"
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "include_images":
                return "includeImages"
            return original_name
        
        # If true, includes preview images (base64 encoded). Defaults to false.
        include_images: Optional[bool] = None

    
    @dataclass
    class SamplesRequestBuilderGetRequestConfiguration(RequestConfiguration[SamplesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

