from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.multipart_body import MultipartBody
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.error_response import ErrorResponse
    from ....models.job_status import JobStatus

class TxtRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/import/txt
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TxtRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/import/txt", path_parameters)
    
    async def post(self,body: MultipartBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[JobStatus]:
        """
        Creates a new job and imports the SpaceGass text file into it.The new job will use the units defined in the imported text file — no conversion is performed.            No job must be open when calling this endpoint. If a job is already open (even an empty one),the request will return 409 Conflict — close the current job first using POST /job/close.            The file should be uploaded as multipart/form-data with the field name "file".            Example usage with curl:                curl -X POST "/api/v1/job/import/txt" /      -F "file=@/path/to/model.txt"
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[JobStatus]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.error_response import ErrorResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ErrorResponse,
            "403": ErrorResponse,
            "404": ErrorResponse,
            "409": ErrorResponse,
            "500": ErrorResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.job_status import JobStatus

        return await self.request_adapter.send_async(request_info, JobStatus, error_mapping)
    
    def to_post_request_information(self,body: MultipartBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new job and imports the SpaceGass text file into it.The new job will use the units defined in the imported text file — no conversion is performed.            No job must be open when calling this endpoint. If a job is already open (even an empty one),the request will return 409 Conflict — close the current job first using POST /job/close.            The file should be uploaded as multipart/form-data with the field name "file".            Example usage with curl:                curl -X POST "/api/v1/job/import/txt" /      -F "file=@/path/to/model.txt"
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "multipart/form-data", body)
        return request_info
    
    def with_url(self,raw_url: str) -> TxtRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TxtRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TxtRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class TxtRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

