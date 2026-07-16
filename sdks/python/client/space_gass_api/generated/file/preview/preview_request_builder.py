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

class PreviewRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /file/preview
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PreviewRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/file/preview{?filePath*,includeImage*}", path_parameters)
    
    # --- @overload added by regen_python_inits.py ---
    @overload
    async def get(
        self,
        *,
        file_path: Optional[str] = None,
        include_image: Optional[bool] = None,
    ) -> Optional[JobFilePreview]: ...
    @overload
    async def get(self, request_configuration: Optional[RequestConfiguration[PreviewRequestBuilderGetQueryParameters]] = None) -> Optional[JobFilePreview]: ...
    # --- end overloads ---
    async def get(self,request_configuration: Optional[RequestConfiguration[PreviewRequestBuilderGetQueryParameters]] = None, **kwargs) -> Optional[JobFilePreview]:
        """
        This endpoint extracts metadata appended to SPACE GASS job files:- Version: SPACE GASS version used to save the file- Licensee: Licensed user name when file was saved- Designer: Computer name where file was saved- Preview image: Screenshot of the model when saved (if available)            Note: Older files may not have this metadata. Metadata fields will be null in that case.            Example usage with curl:                curl -X GET "/api/v1/file/preview?filePath=C:/path/to/job.sg&includeImage=true"
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[JobFilePreview]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.job_file_preview import JobFilePreview

        return await self.request_adapter.send_async(request_info, JobFilePreview, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PreviewRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        This endpoint extracts metadata appended to SPACE GASS job files:- Version: SPACE GASS version used to save the file- Licensee: Licensed user name when file was saved- Designer: Computer name where file was saved- Preview image: Screenshot of the model when saved (if available)            Note: Older files may not have this metadata. Metadata fields will be null in that case.            Example usage with curl:                curl -X GET "/api/v1/file/preview?filePath=C:/path/to/job.sg&includeImage=true"
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> PreviewRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PreviewRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PreviewRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class PreviewRequestBuilderGetQueryParameters():
        """
        This endpoint extracts metadata appended to SPACE GASS job files:- Version: SPACE GASS version used to save the file- Licensee: Licensed user name when file was saved- Designer: Computer name where file was saved- Preview image: Screenshot of the model when saved (if available)            Note: Older files may not have this metadata. Metadata fields will be null in that case.            Example usage with curl:                curl -X GET "/api/v1/file/preview?filePath=C:/path/to/job.sg&includeImage=true"
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "file_path":
                return "filePath"
            if original_name == "include_image":
                return "includeImage"
            return original_name
        
        # Full path to the SPACE GASS job file (.sg or .sgbase)
        file_path: Optional[str] = None

        # If true, includes the preview image (base64 encoded). Defaults to false.
        include_image: Optional[bool] = None

    
    @dataclass
    class PreviewRequestBuilderGetRequestConfiguration(RequestConfiguration[PreviewRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

