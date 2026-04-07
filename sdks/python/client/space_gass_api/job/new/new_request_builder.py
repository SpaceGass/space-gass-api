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
    from ...models.job_status import JobStatus
    from ...models.problem_details import ProblemDetails
    from .new_post_request_body import NewPostRequestBody

class NewRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /job/new
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new NewRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/job/new{?forceCreate*}", path_parameters)
    
    async def post(self,body: NewPostRequestBody, request_configuration: Optional[RequestConfiguration[NewRequestBuilderPostQueryParameters]] = None) -> Optional[JobStatus]:
        """
        Creates a new blank job, or a new job from an uploaded template file (.sgbase).            **Blank job** (no file uploaded):Creates a new empty job with default configuration.            **From template** (file uploaded as multipart/form-data):The template data is loaded but treated as a new job — no file path is set.Use POST /save-as to save to a new location.            If there is an existing job with unsaved changes:- forceCreate=false (default): Returns 409 Conflict- forceCreate=true: Discards unsaved changes and creates new job            Example usage with curl (template):                curl -X POST "/api/v1/job/new?forceCreate=true" /      -F "template=@/path/to/template.sgbase"
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[JobStatus]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.problem_details import ProblemDetails

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ProblemDetails,
            "401": ProblemDetails,
            "409": ProblemDetails,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.job_status import JobStatus

        return await self.request_adapter.send_async(request_info, JobStatus, error_mapping)
    
    def to_post_request_information(self,body: NewPostRequestBody, request_configuration: Optional[RequestConfiguration[NewRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Creates a new blank job, or a new job from an uploaded template file (.sgbase).            **Blank job** (no file uploaded):Creates a new empty job with default configuration.            **From template** (file uploaded as multipart/form-data):The template data is loaded but treated as a new job — no file path is set.Use POST /save-as to save to a new location.            If there is an existing job with unsaved changes:- forceCreate=false (default): Returns 409 Conflict- forceCreate=true: Discards unsaved changes and creates new job            Example usage with curl (template):                curl -X POST "/api/v1/job/new?forceCreate=true" /      -F "template=@/path/to/template.sgbase"
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
    
    def with_url(self,raw_url: str) -> NewRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: NewRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return NewRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class NewRequestBuilderPostQueryParameters():
        """
        Creates a new blank job, or a new job from an uploaded template file (.sgbase).            **Blank job** (no file uploaded):Creates a new empty job with default configuration.            **From template** (file uploaded as multipart/form-data):The template data is loaded but treated as a new job — no file path is set.Use POST /save-as to save to a new location.            If there is an existing job with unsaved changes:- forceCreate=false (default): Returns 409 Conflict- forceCreate=true: Discards unsaved changes and creates new job            Example usage with curl (template):                curl -X POST "/api/v1/job/new?forceCreate=true" /      -F "template=@/path/to/template.sgbase"
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "force_create":
                return "forceCreate"
            return original_name
        
        # If true, discards any existing unsaved job. If false (default), fails if unsaved changes exist.
        force_create: Optional[bool] = None

    
    @dataclass
    class NewRequestBuilderPostRequestConfiguration(RequestConfiguration[NewRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

